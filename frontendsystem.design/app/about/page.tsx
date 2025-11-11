import Link from "next/link";

export default function AboutPage() {
  return (
    <div className="min-h-screen bg-black">
      {/* Hero */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h1 className="text-5xl md:text-6xl font-bold mb-6">About Frontend System Design</h1>
        <p className="text-xl text-gray-400 max-w-3xl leading-relaxed">
          We're on a mission to make system design education accessible to all frontend developers. Our platform provides curated content, interactive learning experiences, and a supportive community.
        </p>
      </div>

      {/* Mission Section */}
      <section className="py-20 bg-gradient-to-r from-gray-900 to-black border-t border-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
            <div>
              <h2 className="text-3xl font-bold mb-6">Our Mission</h2>
              <p className="text-gray-400 mb-4 leading-relaxed">
                Frontend system design is often overlooked, but it's crucial for building scalable and maintainable applications. We believe every developer should have access to high-quality learning resources.
              </p>
              <p className="text-gray-400 leading-relaxed">
                By combining theory with practice, interactive playgrounds with real-world examples, we help developers master the principles of frontend architecture.
              </p>
            </div>
            <div className="space-y-6">
              <div className="bg-gray-900 p-6 rounded-lg border border-gray-800">
                <h3 className="text-lg font-semibold mb-2">📚 Comprehensive Content</h3>
                <p className="text-gray-400">Covering HTML, CSS, JavaScript and modern frontend frameworks</p>
              </div>
              <div className="bg-gray-900 p-6 rounded-lg border border-gray-800">
                <h3 className="text-lg font-semibold mb-2">🚀 Interactive Learning</h3>
                <p className="text-gray-400">Practice with our playground and real-world projects</p>
              </div>
              <div className="bg-gray-900 p-6 rounded-lg border border-gray-800">
                <h3 className="text-lg font-semibold mb-2">👥 Community Driven</h3>
                <p className="text-gray-400">Learn from experts and contribute to the community</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Why Choose Us */}
      <section className="py-20 bg-black">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl font-bold mb-12 text-center">Why Choose Frontend System Design?</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <div className="text-4xl mb-4">🎯</div>
              <h3 className="text-xl font-semibold mb-3">Curated Content</h3>
              <p className="text-gray-400">Handpicked questions and explanations from industry experts</p>
            </div>
            <div>
              <div className="text-4xl mb-4">🔬</div>
              <h3 className="text-xl font-semibold mb-3">Interactive Playground</h3>
              <p className="text-gray-400">Practice coding directly in your browser with live feedback</p>
            </div>
            <div>
              <div className="text-4xl mb-4">🌱</div>
              <h3 className="text-xl font-semibold mb-3">Progressive Learning</h3>
              <p className="text-gray-400">From beginner to advanced, at your own pace</p>
            </div>
            <div>
              <div className="text-4xl mb-4">📈</div>
              <h3 className="text-xl font-semibold mb-3">Real-World Scenarios</h3>
              <p className="text-gray-400">Learn with problems you'll encounter in production</p>
            </div>
            <div>
              <div className="text-4xl mb-4">🤝</div>
              <h3 className="text-xl font-semibold mb-3">Community Support</h3>
              <p className="text-gray-400">Connect with other developers and share knowledge</p>
            </div>
            <div>
              <div className="text-4xl mb-4">✅</div>
              <h3 className="text-xl font-semibold mb-3">Regular Updates</h3>
              <p className="text-gray-400">Fresh content aligned with industry best practices</p>
            </div>
          </div>
        </div>
      </section>

      {/* Learning Path */}
      <section className="py-20 bg-gradient-to-r from-gray-900 to-black border-t border-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl font-bold mb-12 text-center">Our Learning Path</h2>
          <div className="space-y-6">
            <div className="flex gap-6 items-start">
              <div className="w-12 h-12 rounded-full bg-green-900 flex items-center justify-center flex-shrink-0 font-bold text-lg">1</div>
              <div>
                <h3 className="text-xl font-semibold mb-2">Foundations</h3>
                <p className="text-gray-400">Start with HTML, CSS, and JavaScript fundamentals</p>
              </div>
            </div>
            <div className="flex gap-6 items-start">
              <div className="w-12 h-12 rounded-full bg-yellow-900 flex items-center justify-center flex-shrink-0 font-bold text-lg">2</div>
              <div>
                <h3 className="text-xl font-semibold mb-2">Core Concepts</h3>
                <p className="text-gray-400">Deep dive into system design principles and patterns</p>
              </div>
            </div>
            <div className="flex gap-6 items-start">
              <div className="w-12 h-12 rounded-full bg-blue-900 flex items-center justify-center flex-shrink-0 font-bold text-lg">3</div>
              <div>
                <h3 className="text-xl font-semibold mb-2">Advanced Topics</h3>
                <p className="text-gray-400">Explore performance optimization and scalability</p>
              </div>
            </div>
            <div className="flex gap-6 items-start">
              <div className="w-12 h-12 rounded-full bg-purple-900 flex items-center justify-center flex-shrink-0 font-bold text-lg">4</div>
              <div>
                <h3 className="text-xl font-semibold mb-2">Project Building</h3>
                <p className="text-gray-400">Apply your knowledge by building real-world projects</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 bg-black">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-4xl font-bold mb-6">Ready to Master Frontend System Design?</h2>
          <p className="text-xl text-gray-400 mb-8">Join thousands of developers who are already learning with us.</p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/questions"
              className="px-8 py-3 bg-white text-black font-semibold rounded-lg hover:bg-gray-200 transition"
            >
              Start Learning Now
            </Link>
            <Link
              href="/playground"
              className="px-8 py-3 bg-gray-800 text-white font-semibold rounded-lg hover:bg-gray-700 transition border border-gray-700"
            >
              Try Playground
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
