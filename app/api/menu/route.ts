import { NextResponse } from 'next/server'

type SubNutrition = {
  Name: string
  Value: string
  Unit: string | null
}

export type Nutrition = {
  Name: string
  Value: string
  Unit: string | null
  SubList: SubNutrition[] | null
}

type Category = {
  DisplayName: string
}

type Product = {
  MarketingName: string
  ShortDescription: string
  LocationId: string
  StationId: string
  Categories: Category[]
  IsGlutenFree: boolean
  IsKosher: boolean
  IsHalal: boolean
  IsVegan: boolean
  IsVegetarian: boolean
  NutritionalTree: Nutrition[]
}

type Station = {
  StationId: string
  Name: string
}

type MenuProduct = {
  StationId: string
  MenuStations: Station[]
  Product: Product
}

export async function GET() {
  const diningHalls: Record<string, string> = {
    '3314': 'Brandywine',
    '3056': 'Anteatery',
  }

  try {
    // https://uci-campusdish-com.translate.goog/api/menu/GetMenus?locationId=
    const locationIds = Object.keys(diningHalls)
    const fetchData = locationIds.map((locationId) =>
      fetch(
        `https://uci-campusdish-com.translate.goog/api/menu/GetMenus?locationId=${locationId}`
      )
    )

    const responses = await Promise.all(fetchData)

    for (const response of responses) {
      if (!response.ok) {
        throw new Error('Could not fetch CampusDish')
      }
    }

    const menuData = await Promise.all(
      responses.map((response) => response.json())
    )

    // Map stationId's to their names
    const stationKeys: Record<string, string> = {}

    menuData.flatMap((data) =>
      data.Menu.MenuStations.map((station: Station) => {
        stationKeys[station.StationId] = station.Name
      })
    )

    // Get all menu items
    const menu = menuData.flatMap(
      (data) =>
        data.Menu.MenuProducts.map((product: MenuProduct) => {
          const nutritionInfo = product.Product.NutritionalTree.map(
            (nutrient) => ({
              name: nutrient.Name,
              value: nutrient.Value,
              unit: nutrient.Unit,
              subList:
                nutrient.SubList?.map((subNutrient) => ({
                  name: subNutrient.Name,
                  value: subNutrient.Value,
                  unit: subNutrient.Unit,
                })) || null,
            })
          )

          return {
            name: product.Product.MarketingName,
            description:
              product.Product.ShortDescription.split(/\s+/).join(' '),
            category: product.Product.Categories[0]?.DisplayName.trimEnd(),
            diningHall: diningHalls[product.Product.LocationId],
            station: stationKeys[product.StationId],
            isGlutenFree: product.Product.IsGlutenFree,
            isKosher: product.Product.IsKosher,
            isHalal: product.Product.IsHalal,
            isVegan: product.Product.IsVegan,
            isVegetarian: product.Product.IsVegetarian,
            nutrition: nutritionInfo,
          }
        }) || []
    )

    return NextResponse.json(menu)
  } catch (error) {
    return NextResponse.json(
      { error: (error as Error).message },
      { status: 500 }
    )
  }
}
