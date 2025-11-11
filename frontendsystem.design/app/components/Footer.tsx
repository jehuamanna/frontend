import Link from "next/link";

export default function Footer() {
  return (
    <footer className="bg-slate-900 text-slate-100 border-t border-slate-800 mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          {/* Brand */}
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 bg-gradient-to-r from-teal-500 to-blue-500 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">FS</span>
              </div>
              <h3 className="text-lg font-bold">Frontend System</h3>
            </div>
            <p className="text-slate-400 text-sm">Master system design principles for building scalable frontend applications.</p>
          </div>

          {/* Resources */}
          <div>
            <h4 className="font-semibold mb-4 text-white">Resources</h4>
            <ul className="space-y-2 text-slate-400 text-sm">
              <li><a href="#" className="hover:text-teal-400 transition">Questions</a></li>
              <li><a href="#" className="hover:text-teal-400 transition">Workspace</a></li>
              <li><a href="#" className="hover:text-teal-400 transition">Study Plans</a></li>
            </ul>
          </div>

          {/* Company */}
          <div>
            <h4 className="font-semibold mb-4 text-white">Company</h4>
            <ul className="space-y-2 text-slate-400 text-sm">
              <li><a href="#" className="hover:text-teal-400 transition">About Us</a></li>
              <li><a href="#" className="hover:text-teal-400 transition">Blog</a></li>
              <li><a href="#" className="hover:text-teal-400 transition">Contact</a></li>
            </ul>
          </div>

          {/* Connect */}
          <div>
            <h4 className="font-semibold mb-4 text-white">Connect</h4>
            <ul className="space-y-2 text-slate-400 text-sm">
              <li><a href="https://github.com" target="_blank" rel="noopener noreferrer" className="hover:text-teal-400 transition">GitHub</a></li>
              <li><a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="hover:text-teal-400 transition">Twitter</a></li>
              <li><a href="mailto:hello@frontendsystem.design" className="hover:text-teal-400 transition">Email</a></li>
            </ul>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-slate-800 pt-8 mt-8">
          <div className="flex flex-col md:flex-row justify-between items-center text-slate-400 text-sm">
            <p>Copyright 2025 Frontend System Design. All rights reserved.</p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              <a href="#" className="hover:text-teal-400 transition">Privacy Policy</a>
              <a href="#" className="hover:text-teal-400 transition">Terms of Service</a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
