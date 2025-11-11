import Link from "next/link";

export default function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center justify-center bg-black overflow-hidden pt-20">
      {/* Background gradient effect */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute w-96 h-96 bg-white/5 rounded-full blur-3xl -top-20 -left-20"></div>
        <div className="absolute w-96 h-96 bg-white/5 rounded-full blur-3xl -bottom-20 -right-20"></div>
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div className="mb-6">
          <span className="inline-block px-4 py-2 bg-gray-900 border border-gray-800 rounded-full text-sm text-gray-300 mb-6">
            ✨ Welcome to Frontend System Design
          </span>
        </div>

        <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
          Master Frontend <br />
          <span className="bg-gradient-to-r from-white via-gray-300 to-white bg-clip-text text-transparent">
            System Design
          </span>
        </h1>

        <p className="text-xl text-gray-400 mb-8 max-w-2xl mx-auto leading-relaxed">
          Learn system design principles for building scalable, efficient, and maintainable frontend applications. Master HTML, CSS, and JavaScript through curated questions and hands-on projects.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
          <Link
            href="/questions"
            className="px-8 py-4 bg-white text-black font-semibold rounded-lg hover:bg-gray-200 transition transform hover:scale-105"
          >
            Start Learning
          </Link>
          <Link
            href="/playground"
            className="px-8 py-4 bg-gray-900 text-white font-semibold rounded-lg hover:bg-gray-800 transition border border-gray-800"
          >
            Open Playground
          </Link>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-4 text-center">
          <div>
            <p className="text-2xl font-bold text-white">100+</p>
            <p className="text-gray-400 text-sm">Questions</p>
          </div>
          <div>
            <p className="text-2xl font-bold text-white">3</p>
            <p className="text-gray-400 text-sm">Core Topics</p>
          </div>
          <div>
            <p className="text-2xl font-bold text-white">∞</p>
            <p className="text-gray-400 text-sm">Learning Path</p>
          </div>
        </div>
      </div>

      {/* Scroll indicator */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
        <svg className="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
        </svg>
      </div>
    </section>
  );
}
