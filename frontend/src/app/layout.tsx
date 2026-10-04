import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "PatchPal Security Digest",
  description: "A friend's security digest powered by local AI",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-[#f7f5f2]">
        <header className="sticky top-0 z-10 border-b border-[#e5e0da] bg-[#f7f5f2]/80 backdrop-blur">
          <div className="mx-auto flex max-w-5xl items-center justify-between p-4">
            <a href="/" className="text-xl font-bold tracking-tight text-[#1f1f1f]">
              PatchPal
            </a>
            <nav className="flex gap-6 text-base text-zinc-600">
              <a href="/" className="hover:text-[#c97d4b]">Digest</a>
              <a href="/profile" className="hover:text-[#c97d4b]">Profile</a>
            </nav>
          </div>
        </header>
        {children}
      </body>
    </html>
  );
}
