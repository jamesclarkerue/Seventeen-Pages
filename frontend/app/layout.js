import './globals.css'

export const metadata = {
  title: 'Seventeen Pages - AI Manuscript Editing',
  description: 'Professional manuscript editing powered by AI. Get expert feedback on your writing with critique, line editing, copyediting, and proofreading.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
