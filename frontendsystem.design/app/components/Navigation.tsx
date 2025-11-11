"use client";

import Link from "next/link";
import { useState } from "react";

export default function Navigation() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gradient-to-r from-teal-600 to-blue-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-lg">FS</span>
            </div>
            <span className="text-lg font-bold text-slate-900 hidden sm:inline">Frontend System</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex space-x-8">
            <a href="#" className="text-slate-600 hover:text-teal-600 transition text-sm font-medium">Features</a>
            <a href="#" className="text-slate-600 hover:text-teal-600 transition text-sm font-medium">Questions</a>
            <a href="#" className="text-slate-600 hover:text-teal-600 transition text-sm font-medium">Pricing</a>
            <a href="#" className="text-slate-600 hover:text-teal-600 transition text-sm font-medium">About</a>
          </div>

          {/* CTA Button */}
          <div className="hidden md:block">
            <button className="px-4 py-2 bg-gradient-to-r from-teal-600 to-blue-600 text-white rounded-lg hover:shadow-md transition text-sm font-medium">
              Sign In
            </button>
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden p-2 rounded-lg hover:bg-slate-100"
          >
            <svg className="w-6 h-6 text-slate-900" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="md:hidden pb-4 space-y-2">
            <a href="#" className="block px-4 py-2 text-slate-600 hover:text-teal-600 hover:bg-slate-50 rounded transition">Features</a>
            <a href="#" className="block px-4 py-2 text-slate-600 hover:text-teal-600 hover:bg-slate-50 rounded transition">Questions</a>
            <a href="#" className="block px-4 py-2 text-slate-600 hover:text-teal-600 hover:bg-slate-50 rounded transition">Pricing</a>
            <a href="#" className="block px-4 py-2 text-slate-600 hover:text-teal-600 hover:bg-slate-50 rounded transition">About</a>
          </div>
        )}
      </div>
    </nav>
  );
}
