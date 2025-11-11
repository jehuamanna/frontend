"use client";

import { useState } from "react";

export default function PlaygroundPage() {
  const [html, setHtml] = useState(`<div class="container">
  <h1>Welcome to Frontend Playground</h1>
  <p>Write your HTML, CSS, and JavaScript code here!</p>
  <button id="myBtn">Click me</button>
</div>`);

  const [css, setCss] = useState(`* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  text-align: center;
  max-width: 500px;
}

h1 {
  color: #333;
  margin-bottom: 20px;
  font-size: 2em;
}

p {
  color: #666;
  margin-bottom: 30px;
  line-height: 1.6;
}

button {
  background: #667eea;
  color: white;
  border: none;
  padding: 12px 30px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
  font-weight: 600;
  transition: transform 0.3s, box-shadow 0.3s;
}

button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}`);

  const [js, setJs] = useState(`document.getElementById('myBtn').addEventListener('click', function() {
  alert('Button clicked! System Design Playground is working.');
  this.style.background = '#764ba2';
});`);

  const srcDoc = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Playground Preview</title>
      <style>
        ${css}
      </style>
    </head>
    <body>
      ${html}
      <script>
        ${js}
      </script>
    </body>
    </html>
  `;

  return (
    <div className="min-h-screen bg-black">
      {/* Header */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 border-b border-gray-800">
        <h1 className="text-4xl font-bold mb-2">Interactive Playground</h1>
        <p className="text-gray-400">Write and test your HTML, CSS, and JavaScript code in real-time.</p>
      </div>

      {/* Playground */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* HTML Editor */}
          <div className="bg-gray-900 rounded-lg border border-gray-800 overflow-hidden">
            <div className="bg-gray-800 px-4 py-3 border-b border-gray-700">
              <h3 className="font-semibold text-orange-400 flex items-center gap-2">
                <span className="text-lg">🔶</span> HTML
              </h3>
            </div>
            <textarea
              value={html}
              onChange={(e) => setHtml(e.target.value)}
              className="w-full h-64 p-4 bg-gray-900 text-gray-100 font-mono text-sm resize-none focus:outline-none border-none"
              placeholder="Enter your HTML here..."
            />
          </div>

          {/* CSS Editor */}
          <div className="bg-gray-900 rounded-lg border border-gray-800 overflow-hidden">
            <div className="bg-gray-800 px-4 py-3 border-b border-gray-700">
              <h3 className="font-semibold text-blue-400 flex items-center gap-2">
                <span className="text-lg">🔵</span> CSS
              </h3>
            </div>
            <textarea
              value={css}
              onChange={(e) => setCss(e.target.value)}
              className="w-full h-64 p-4 bg-gray-900 text-gray-100 font-mono text-sm resize-none focus:outline-none border-none"
              placeholder="Enter your CSS here..."
            />
          </div>

          {/* JavaScript Editor */}
          <div className="bg-gray-900 rounded-lg border border-gray-800 overflow-hidden">
            <div className="bg-gray-800 px-4 py-3 border-b border-gray-700">
              <h3 className="font-semibold text-yellow-400 flex items-center gap-2">
                <span className="text-lg">🟡</span> JavaScript
              </h3>
            </div>
            <textarea
              value={js}
              onChange={(e) => setJs(e.target.value)}
              className="w-full h-64 p-4 bg-gray-900 text-gray-100 font-mono text-sm resize-none focus:outline-none border-none"
              placeholder="Enter your JavaScript here..."
            />
          </div>
        </div>

        {/* Preview */}
        <div className="mt-8">
          <div className="bg-gray-900 rounded-lg border border-gray-800 overflow-hidden">
            <div className="bg-gray-800 px-4 py-3 border-b border-gray-700">
              <h3 className="font-semibold text-green-400 flex items-center gap-2">
                <span className="text-lg">👁️</span> Live Preview
              </h3>
            </div>
            <iframe
              srcDoc={srcDoc}
              title="preview"
              className="w-full h-96 bg-white"
              sandbox="allow-scripts"
            />
          </div>
        </div>

        {/* Tips */}
        <div className="mt-8 bg-gray-900/50 border border-gray-800 rounded-lg p-6">
          <h3 className="text-lg font-semibold mb-4">💡 Tips for using the Playground</h3>
          <ul className="space-y-2 text-gray-300">
            <li>✓ Edit HTML, CSS, and JavaScript in real-time</li>
            <li>✓ See live updates in the preview pane</li>
            <li>✓ Use this to test and practice frontend concepts</li>
            <li>✓ Experiment with responsive design and interactions</li>
            <li>✓ Save your code locally for reference</li>
          </ul>
        </div>
      </div>
    </div>
  );
}
