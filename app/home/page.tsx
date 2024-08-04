'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'

import FoodItemCard from '../components/FoodItemCard'
import { Nutrition } from '../api/menu/route'

type FoodItem = {
  name: string
  description: string
  category: string
  diningHall: string
  station: string
  isGlutenFree: boolean
  isKosher: boolean
  isHalal: boolean
  isVegan: boolean
  isVegetarian: boolean
  nutrition: Nutrition
}

export default function Home() {
  const [menuItems, setMenuItems] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchFoodItems = async () => {
      try {
        const response = await fetch('api/menu')
        const data = await response.json()

        setMenuItems(data)
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
          {menuItems.map((item: FoodItem, index) => (
            <Link
              href={{
                pathname: `/food/${item.name.replace(/\s+/g, '-').toLowerCase()}`,
              }}
            >
              <FoodItemCard
                foodName={item.name}
                location={item.diningHall}
                rating={3.5}
                imagePath=""
                key={index}
              />
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}
