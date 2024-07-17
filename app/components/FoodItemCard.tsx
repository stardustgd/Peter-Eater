import { FaStar, FaStarHalfAlt as FaStarHalf, FaRegStar } from 'react-icons/fa'
import Image from 'next/image'

export default function FoodItemCard() {
  return (
    <div className="flex flex-col relative justify-between rounded-[20px] w-60 h-60 shadow-xl">
      <Image
        src="/food_placeholder.jpg"
        alt="Food name"
        layout="fill"
        objectFit="cover"
        className="rounded-[20px]"
      />
      <div className="absolute flex flex-col justify-between rounded-[20px] w-full h-full p-3 bg-[#123459a6] backdrop-blur-[1px]">
        <div className="self-start rounded-full inline-block px-3 py-1 bg-[#888]">
          <h1 className="text-xl text-white">Anteatery</h1>
        </div>
        <div className="flex flex-col items-center">
          <h1 className="text-3xl">Food Name</h1>
          <div className="flex flex-row">
            <FaStar className="fill-yellow-300" />
            <FaStar className="fill-yellow-300" />
            <FaStarHalf className="fill-yellow-300" />
            <FaRegStar className="fill-yellow-300" />
            <FaRegStar className="fill-yellow-300" />
          </div>
        </div>
      </div>
    </div>
  )
}
