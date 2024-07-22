'use client'
import { useEffect, useState } from 'react'

import FoodItemCard from '../components/FoodItemCard'

interface Food {
  foodName: string
  foodDescription: string
  calories?: string
  category?: string
}

interface Location {
  foods: Food[]
  station: string
  diningHall: string
}

export default function Home() {
  const [foodItems, setFoodItems] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchFoodItems = async () => {
      try {
        const response = await fetch('api/menu')
        const data = await response.json()

        console.log(data)

        setFoodItems(data)
      } catch (error) {
        console.error('Error fetching food items:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchFoodItems()
  }, [])

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <h1 className="text-black">Loading...</h1>
      </div>
    )
  }
  return (
    <div className="h-screen">
      <div className="flex flex-col md:flex-row gap-3 justify-center items-center py-5">
        <div className="flex flex-row flex-wrap gap-3 justify-center">
          {foodItems.map((location: Location) =>
            location.foods.map((food) => (
              <FoodItemCard
                foodName={food.foodName}
                rating={3.5}
                imagePath=""
                location={location.diningHall}
              />
            ))
          )}
        </div>
      </div>
    </div>
  )
}
