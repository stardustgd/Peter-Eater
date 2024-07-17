import FoodItemCard from '../components/FoodItemCard'

export default function Home() {
  return (
    <div className="h-screen">
      <div className="flex flex-col md:flex-row gap-3 justify-center items-center py-5">
        <FoodItemCard />
        <FoodItemCard />
        <FoodItemCard />
        <FoodItemCard />
      </div>
    </div>
  )
}
