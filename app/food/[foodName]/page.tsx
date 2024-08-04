export default function Page({ params }: { params: { foodName: string } }) {
  return <div>{params.foodName.replaceAll('-', ' ')}</div>
}
