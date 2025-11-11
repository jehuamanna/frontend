import type { Metadata, Viewport } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Footer from "./components/Footer";

const geist = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  title: "Frontend System Design - Master HTML, CSS & JavaScript",
  description: "Learn system design principles for building scalable frontend applications. Curated questions, interactive playground, and real-world examples.",
  keywords: "frontend, system design, HTML, CSS, JavaScript, web development, scalable applications",
  authors: [{ name: "Frontend System Design" }],
  robots: "index, follow",
  openGraph: {
    title: "Frontend System Design",
    description: "Master system design for frontend development",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <link rel="canonical" href="https://frontendsystem.design" />
      </head>
      <body className={`${geist.variable} ${geistMono.variable} bg-white text-slate-900 antialiased`}>
        <main className="min-h-screen">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
