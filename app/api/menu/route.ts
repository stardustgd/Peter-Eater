import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url)
    const location = searchParams.get('location') || 'brandywine'

    const query = new URLSearchParams({ location }).toString()
    const url = `https://zotmeal-backend.vercel.app/api?${query}`

    const response = await fetch(url)

    if (!response.ok) throw new Error('Could not fetch ZotMeal data')

    const data = await response.json()

    const completeMenu = data.all.map((location: any) => {
      const diningHall = data.restaurant
      const station = location.station
      const allFoods = location.menu.flatMap((menu: any) => {
        const category = menu.category

        return menu.items.map((item: any) => ({
          foodName: item.name,
          foodDescription: item.description,
          calories: item.nutrition?.calories || 'N/A',
          category,
        }))
      })

      return { foods: allFoods, station, diningHall }
    })

    return NextResponse.json(completeMenu)
  } catch (error) {
    return NextResponse.json(
      { error: (error as Error).message },
      { status: 500 }
    )
  }
}
