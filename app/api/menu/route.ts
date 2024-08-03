import { NextResponse } from 'next/server'

export async function GET() {
  const diningHalls: Record<string, string> = {
    '3314': 'Brandywine',
    '3056': 'Anteatery',
  }

  try {
    // https://uci-campusdish-com.translate.goog/api/menu/GetMenus?locationId=
    const response = await fetch(
      'https://uci-campusdish-com.translate.goog/api/menu/GetMenus?locationId=3314'
    )

    if (!response.ok) {
      throw new Error('Could not fetch CampusDish')
    }

    const data = await response.json()

    const menu =
      data.Menu.MenuProducts.map((product) => ({
        name: product.Product.MarketingName,
        description: product.Product.ShortDescription.split(/\s+/).join(' '),
        calories: product.Product.NutritionalTree[0].Value,
        category: product.Product.Categories[0]?.DisplayName.trimEnd(),
        diningHall: diningHalls[product.Product.LocationId],
        station: product.StationId,
      })) || []

    return NextResponse.json(menu)
  } catch (error) {
    return NextResponse.json(
      { error: (error as Error).message },
      { status: 500 }
    )
  }
}
