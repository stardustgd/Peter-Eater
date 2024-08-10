import type { Metadata } from 'next'
import { DM_Sans } from 'next/font/google'
import './globals.css'

const dm_sans = DM_Sans({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Peter Eater',
  description: 'UCI Dining Hall rating service',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={dm_sans.className}>{children}</body>
    </html>
  )
}
