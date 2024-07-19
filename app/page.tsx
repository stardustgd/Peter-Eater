import Image from 'next/image'
import Link from 'next/link'
import { FaArrowRight } from 'react-icons/fa6'

export default function Home() {
  return (
    <div className="relative flex flex-col justify-center items-center h-screen">
      <Image
        src="/brandywine.png"
        alt=""
        height={1920}
        width={1080}
        className="object-cover w-full h-screen"
      />
      <div className="absolute top-0 left-0 right-0 bottom-0 w-full h-screen bg-[#0064a480] backdrop-blur-sm flex flex-col">
        <div className="shadow-2xl bg-[#002244bf] backdrop-blur-sm">
          <div className="px-4 md:px-24 py-4 flex flex-row items-center">
            <Image src="/petereater.png" alt="" width={50} height={50} />
            <h1 className="px-4 md:px-12 text-4xl">Peter Eater</h1>
          </div>
        </div>
        <div className="flex flex-col my-auto pb-24 justify-center items-center">
          <h1 className="text-center">
            UCI's <span className="text-[#FECC07]">#1</span> Dining Hall Rating
            Service
          </h1>
          <Link href="home/">
            <button className="bg-[#FECC07] max-w-fit text-white font-bold py-3 px-6 rounded-full">
              <FaArrowRight className="size-5" />
            </button>
          </Link>
        </div>
      </div>
    </div>
  )
}
