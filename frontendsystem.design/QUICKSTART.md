# Quick Start Guide - Frontend System Design

Get up and running with the Frontend System Design platform in just a few minutes!

## ⚡ 5-Minute Setup

### Prerequisites
- Node.js 18+ installed
- Git installed
- A code editor (VS Code recommended)

### Step 1: Clone & Install
```bash
# Clone the repository
git clone https://github.com/yourusername/frontendsystem.design.git
cd frontendsystem.design

# Install dependencies
npm install
```

### Step 2: Run Development Server
```bash
npm run dev
```

### Step 3: Open in Browser
Visit `http://localhost:3000` in your browser. You'll see the homepage with:
- Beautiful hero section
- Feature overview
- Navigation to different sections

## 🚀 What You Can Do

### 1. **Explore Questions**
- Visit `/questions` page
- Filter by HTML, CSS, or JavaScript
- See 16 system design questions with difficulty levels
- Each question has a description and category tag

### 2. **Use the Playground**
- Go to `/playground`
- Edit HTML, CSS, and JavaScript in real-time
- See live preview updates instantly
- Perfect for testing code ideas

### 3. **Learn About the Platform**
- Visit `/about` page
- Understand the learning path
- See why to choose this platform

## 📁 Project Structure

```
frontendsystem.design/
├── app/
│   ├── components/          # Reusable components
│   │   ├── Navigation.tsx
│   │   ├── Footer.tsx
│   │   ├── HeroSection.tsx
│   │   └── FeatureCard.tsx
│   ├── questions/           # Questions page
│   │   └── page.tsx
│   ├── playground/          # Playground page
│   │   └── page.tsx
│   ├── about/              # About page
│   │   └── page.tsx
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Home page
│   ├── globals.css         # Global styles
│   └── sitemap.ts          # SEO sitemap
├── public/
│   └── robots.txt          # Search engine crawling
├── README.md               # Full documentation
├── DEPLOYMENT.md           # Deployment guide
└── package.json            # Dependencies
```

## 🎨 Customization

### Change Colors
Edit Tailwind classes in component files. The site uses:
- `bg-black` for backgrounds
- `text-white` for text
- `border-gray-800` for borders

### Add More Questions
Edit `/app/questions/page.tsx`:
```typescript
const questions: Question[] = [
  {
    id: 17,
    title: "Your New Question",
    category: "html", // or "css", "javascript"
    difficulty: "beginner", // or "intermediate", "advanced"
    description: "Question description",
    slug: "question-slug",
  },
  // ... more questions
];
```

### Update Content
- Navigation links: `/app/components/Navigation.tsx`
- Footer links: `/app/components/Footer.tsx`
- Homepage text: `/app/page.tsx`
- About page: `/app/about/page.tsx`

## 🚢 Deploy in 5 Minutes

### Using Vercel (Recommended)
1. Push code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Select your repository
5. Click "Deploy" - Done! 🎉

Your site is now live at `https://[project-name].vercel.app`

See `DEPLOYMENT.md` for other deployment options.

## 📝 Available Commands

```bash
# Development
npm run dev              # Start dev server at http://localhost:3000

# Production
npm run build           # Build for production
npm start              # Start production server

# Code Quality
npm run lint           # Run ESLint
npm run lint -- --fix  # Auto-fix linting issues
```

## 🐛 Troubleshooting

### Port 3000 is already in use
```bash
# On Linux/Mac:
lsof -ti:3000 | xargs kill -9

# Then restart:
npm run dev
```

### Dependencies not installed
```bash
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Build fails
```bash
# Clean build
rm -rf .next
npm run build
```

## 📚 Learn More

- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [React Documentation](https://react.dev)
- [TypeScript Documentation](https://www.typescriptlang.org/docs)

## 🎯 Next Steps

1. ✅ Run the project locally
2. ✅ Explore all pages
3. ✅ Test the playground
4. ✅ Customize for your needs
5. ✅ Deploy to production

## 💡 Pro Tips

1. **Use TypeScript**: Leverage type safety for better development
2. **Mobile First**: Always test on mobile devices
3. **SEO**: Content is already SEO optimized with metadata
4. **Performance**: Next.js handles optimization automatically
5. **Deployment**: Use Vercel for the best Next.js experience

## 🤝 Need Help?

- Check `README.md` for comprehensive documentation
- See `DEPLOYMENT.md` for deployment help
- Review component code in `app/components/`
- Check official Next.js docs

---

**Ready to build?** Start with `npm run dev` and explore! 🚀
