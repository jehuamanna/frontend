"use client";

import { useState } from "react";
import Link from "next/link";

interface Question {
  id: number;
  title: string;
  category: "html" | "css" | "javascript";
  difficulty: "beginner" | "intermediate" | "advanced";
  description: string;
  slug: string;
}

const questions: Question[] = [
  // HTML Questions
  {
    id: 1,
    title: "Semantic HTML Structure",
    category: "html",
    difficulty: "beginner",
    description: "Design a semantic HTML structure for a complex web application",
    slug: "semantic-html-structure",
  },
  {
    id: 2,
    title: "Form Design Patterns",
    category: "html",
    difficulty: "intermediate",
    description: "Create accessible and scalable form systems",
    slug: "form-design-patterns",
  },
  {
    id: 3,
    title: "Meta Tags & SEO",
    category: "html",
    difficulty: "beginner",
    description: "Implement comprehensive SEO meta tags strategy",
    slug: "meta-tags-seo",
  },
  {
    id: 4,
    title: "Accessibility (a11y) Design",
    category: "html",
    difficulty: "intermediate",
    description: "Build fully accessible HTML structures following WCAG guidelines",
    slug: "accessibility-design",
  },
  {
    id: 5,
    title: "Web Components Architecture",
    category: "html",
    difficulty: "advanced",
    description: "Design scalable web component systems",
    slug: "web-components-architecture",
  },

  // CSS Questions
  {
    id: 6,
    title: "Responsive Design System",
    category: "css",
    difficulty: "intermediate",
    description: "Design a comprehensive responsive CSS system for multiple devices",
    slug: "responsive-design-system",
  },
  {
    id: 7,
    title: "CSS Architecture & Scalability",
    category: "css",
    difficulty: "intermediate",
    description: "Build scalable CSS architectures (BEM, SMACSS, Utility-First)",
    slug: "css-architecture-scalability",
  },
  {
    id: 8,
    title: "Performance Optimization",
    category: "css",
    difficulty: "advanced",
    description: "Optimize CSS for performance and rendering",
    slug: "css-performance-optimization",
  },
  {
    id: 9,
    title: "Layout Systems",
    category: "css",
    difficulty: "intermediate",
    description: "Design flexible layout systems using Flexbox and Grid",
    slug: "layout-systems",
  },
  {
    id: 10,
    title: "Animation & Transitions",
    category: "css",
    difficulty: "intermediate",
    description: "Build performant animation systems",
    slug: "animation-transitions",
  },

  // JavaScript Questions
  {
    id: 11,
    title: "State Management Architecture",
    category: "javascript",
    difficulty: "advanced",
    description: "Design scalable state management systems",
    slug: "state-management-architecture",
  },
  {
    id: 12,
    title: "Component Lifecycle Management",
    category: "javascript",
    difficulty: "intermediate",
    description: "Manage complex component lifecycles efficiently",
    slug: "component-lifecycle-management",
  },
  {
    id: 13,
    title: "Event Handling & Delegation",
    category: "javascript",
    difficulty: "intermediate",
    description: "Implement efficient event systems at scale",
    slug: "event-handling-delegation",
  },
  {
    id: 14,
    title: "Memory Management & Performance",
    category: "javascript",
    difficulty: "advanced",
    description: "Prevent memory leaks and optimize performance",
    slug: "memory-management-performance",
  },
  {
    id: 15,
    title: "Asynchronous Patterns",
    category: "javascript",
    difficulty: "intermediate",
    description: "Design robust async/await and Promise patterns",
    slug: "asynchronous-patterns",
  },
  {
    id: 16,
    title: "Module System Design",
    category: "javascript",
    difficulty: "intermediate",
    description: "Build modular, maintainable JavaScript applications",
    slug: "module-system-design",
  },
];

const categoryLabels = {
  html: "HTML",
  css: "CSS",
  javascript: "JavaScript",
};

const difficultyColors = {
  beginner: "bg-green-900/30 text-green-300 border-green-800",
  intermediate: "bg-yellow-900/30 text-yellow-300 border-yellow-800",
  advanced: "bg-red-900/30 text-red-300 border-red-800",
};

export default function QuestionsPage() {
  const [selectedCategory, setSelectedCategory] = useState<"all" | "html" | "css" | "javascript">("all");

  const filteredQuestions = selectedCategory === "all" 
    ? questions 
    : questions.filter(q => q.category === selectedCategory);

  return (
    <div className="min-h-screen bg-black">
      {/* Header */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">System Design Questions</h1>
        <p className="text-gray-400 text-lg">
          Master frontend system design with our curated collection of questions covering HTML, CSS, and JavaScript.
        </p>
      </div>

      {/* Filter Tabs */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-12">
        <div className="flex flex-wrap gap-3">
          {["all", "html", "css", "javascript"].map((category) => (
            <button
              key={category}
              onClick={() => setSelectedCategory(category as any)}
              className={`px-6 py-2 rounded-lg font-medium transition ${
                selectedCategory === category
                  ? "bg-white text-black"
                  : "bg-gray-900 text-gray-300 hover:bg-gray-800 border border-gray-800"
              }`}
            >
              {category === "all" ? "All Questions" : categoryLabels[category as keyof typeof categoryLabels]}
            </button>
          ))}
        </div>
      </div>

      {/* Questions Grid */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
        <div className="grid gap-4">
          {filteredQuestions.map((question) => (
            <Link key={question.id} href={`/questions/${question.slug}`}>
              <div className="p-6 rounded-lg bg-gray-900/50 border border-gray-800 hover:border-gray-700 hover:bg-gray-900 transition cursor-pointer group">
                <div className="flex items-start justify-between gap-4 mb-4">
                  <div className="flex-1">
                    <h3 className="text-xl font-semibold text-white group-hover:text-gray-200 transition mb-2">
                      {question.title}
                    </h3>
                    <p className="text-gray-400">{question.description}</p>
                  </div>
                  <div className="flex gap-2">
                    <span className={`px-3 py-1 rounded-full text-sm font-medium border ${difficultyColors[question.difficulty]}`}>
                      {question.difficulty.charAt(0).toUpperCase() + question.difficulty.slice(1)}
                    </span>
                    <span className="px-3 py-1 rounded-full text-sm font-medium bg-blue-900/30 text-blue-300 border border-blue-800">
                      {categoryLabels[question.category]}
                    </span>
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}
