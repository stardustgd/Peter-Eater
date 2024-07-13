import Image from 'next/image'

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
      <div className="absolute top-0 left-0 right-0 bottom-0 w-full h-screen bg-[#0064a480] backdrop-blur-sm flex flex-col justify-center items-center">
        <h1 className="">Peter Eater</h1>
        <h2 className="">#1 UCI Dining hall rating service</h2>
        <button className="bg-blue-500 max-w-fit text-white font-bold py-2 px-4 rounded-full">
          Start!
        </button>
      </div>
    </div>
  )
}
