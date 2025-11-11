# Coming Soon Promotional Website - Complete Setup Guide

Your Frontend System Design website is now a professional "Coming Soon" landing page with email subscription management powered by Supabase.

## What's New

This redesigned version features:
- Professional coming soon promotional design
- Zero emojis for a premium look
- Email + username subscription form
- Supabase database integration
- Modern gradient backgrounds
- Feature preview cards
- Subscriber tracking dashboard

## Quick Start

### 1. Install Dependencies

All dependencies are already installed, but to verify:

```bash
npm install
```

### 2. Set Up Supabase

Follow the detailed guide in `SUPABASE_SETUP.md` to:
1. Create a Supabase account
2. Create a new project
3. Create the subscribers table
4. Get your API keys
5. Configure environment variables

### 3. Configure Environment Variables

Create a `.env.local` file in the project root:

```bash
NEXT_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
```

**Important:** This file is in `.gitignore` and won't be committed to version control.

### 4. Start Development Server

```bash
npm run dev
```

Visit `http://localhost:3000` to see your coming soon page.

### 5. Test the Form

1. Scroll down to the subscription form
2. Enter a username and email
3. Click "Get Early Access"
4. You should see a success message
5. Check your Supabase dashboard to verify the data was saved

## Project Structure

```
app/
├── components/
│   ├── Navigation.tsx        (Updated for coming soon)
│   ├── Footer.tsx            (Simplified footer)
│   └── SubscriptionForm.tsx   (Email form - NEW)
├── actions/
│   └── subscribe.ts          (Server action - NEW)
├── page.tsx                  (Coming soon landing page - REDESIGNED)
└── layout.tsx

lib/
└── supabase.ts              (Supabase client - NEW)

.env.example                 (Environment template - NEW)
SUPABASE_SETUP.md            (Supabase guide - NEW)
```

## Features

### 1. Professional Design
- Premium black background with white/gray text
- Gradient accents (blue and purple)
- Glassmorphism effects with backdrop blur
- Smooth hover animations
- Responsive across all devices

### 2. Subscription Form
- Username input field
- Email input field
- Real-time validation
- Success/error messaging
- Loading states
- Accessible design

### 3. Coming Soon Messaging
- "Coming Soon" badge
- "Don't Miss the Launch" CTA
- Early bird pricing promise
- Launch date (Q1 2025)
- Feature preview cards

### 4. Social Proof
- Waitlist member count
- Expert contributor count
- Daily visitor count
- Official launch date

### 5. Feature Cards
- 6 feature previews with icons
- Hover effects
- Clean typography
- Professional styling

## Customization

### Change Text Content

Edit `app/page.tsx`:

```typescript
// Main heading
<h1>Master Frontend System Design</h1>

// Subheading
<p>Learn system design principles...</p>

// Feature descriptions
// Change the "What to Expect" section
```

### Change Colors

The theme uses Tailwind classes:
- `bg-black` - Primary background
- `text-white` - Primary text
- `border-white/10` - Primary borders
- `bg-white/5` - Secondary backgrounds

To change to a different color scheme, update Tailwind classes throughout the components.

### Change Feature Icons

In `app/page.tsx`, find the "What to Expect" section and modify the SVG divs:

```tsx
{/* Custom icon */}
<div className="w-12 h-12 rounded-lg bg-white/10 flex items-center justify-center mb-4 group-hover:bg-white/20 transition">
  {/* Replace this div with your custom icon */}
  <div>Your Icon Here</div>
</div>
```

### Customize Form Fields

In `app/components/SubscriptionForm.tsx`:

```typescript
// Add or remove form fields
// Change placeholder text
// Customize validation
// Change button text
```

### Update Form Action

In `app/actions/subscribe.ts`:

```typescript
// Modify validation rules
// Add more form fields
// Customize error messages
// Add email notifications
```

## Supabase Integration

### Database Schema

The subscribers table has:
- `id` - Unique identifier (UUID)
- `username` - User's chosen username
- `email` - User's email (unique constraint)
- `created_at` - Subscription timestamp
- `updated_at` - Last update timestamp

### Row Level Security

The database is configured with RLS policies that allow:
- Anyone to insert new subscribers
- Anyone to read subscriber data (optional)

This is secure because the anon key is restricted by these policies.

### Managing Subscribers

1. **View subscribers:**
   - Go to Supabase dashboard
   - Table Editor → subscribers
   - Browse all subscriber data

2. **Export data:**
   - Select all rows
   - Click menu → Download as CSV
   - Import into email service

3. **Send emails:**
   - Connect to email service (SendGrid, Mailchimp, etc.)
   - Import CSV of subscribers
   - Send launch notifications

## Deployment

### Deploy to Vercel (Recommended)

1. Push code to GitHub
2. Connect to Vercel
3. Add environment variables in Vercel dashboard:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
4. Deploy - Done!

### Deploy to Other Platforms

See `DEPLOYMENT.md` for instructions on:
- Netlify
- AWS Amplify
- Google Cloud Run
- Docker + Custom Server

## Monitoring

### Subscriber Growth

Track in Supabase:
1. Go to Table Editor
2. Click "subscribers"
3. Watch row count grow as people subscribe

### Error Handling

Check browser console for errors:
1. Open DevTools (F12)
2. Go to Console tab
3. Look for error messages
4. Report issues with full error text

### Analytics

Add Google Analytics:
1. Add GA script to `app/layout.tsx`
2. Track form submissions
3. Monitor page views
4. Track signup conversions

## Best Practices

1. **Email Verification**
   - Consider adding email verification
   - Reduces invalid emails

2. **Double Opt-In**
   - Send confirmation email
   - Users click link to confirm
   - Improves list quality

3. **Content Personalization**
   - Store preferences with user
   - Send targeted launch emails
   - Improve engagement

4. **Rate Limiting**
   - Add per-IP rate limiting
   - Prevent form spam
   - Protect your database

5. **Newsletter Integration**
   - Export to Mailchimp, SendGrid, etc.
   - Segment subscribers
   - Send campaigns

## Common Tasks

### Add a New Form Field

1. Edit `SubscriptionForm.tsx`
2. Add input field
3. Update state
4. Update form submission
5. Modify Supabase action
6. Update database schema

### Send Confirmation Email

1. Set up email service (SendGrid, Mailgun)
2. Create email template
3. Call email API in subscribe action
4. Add success feedback

### Customize Success Message

Edit `SubscriptionForm.tsx`:

```typescript
// Change this message
message: 'Successfully subscribed! Check your email for updates.'
```

### Set Subscriber Limit

Add check in `app/actions/subscribe.ts`:

```typescript
// Check total subscriber count
// Return error if limit reached
```

## Troubleshooting

### Form Not Submitting

1. Check browser console for errors
2. Verify `.env.local` file exists
3. Verify Supabase credentials are correct
4. Restart dev server

### "Missing environment variables" Error

1. Create `.env.local` file
2. Add Supabase URL and key
3. Restart dev server
4. Clear browser cache

### Supabase Connection Errors

1. Check internet connection
2. Verify Supabase project is active
3. Check API key is correct
4. Try in incognito mode

### Emails Not Saving

1. Check Supabase dashboard
2. Verify table exists
3. Check RLS policies
4. Look for SQL errors

## Next Steps

1. Customize the design to match your brand
2. Set up Supabase (see SUPABASE_SETUP.md)
3. Test the form locally
4. Deploy to production
5. Add custom domain
6. Monitor subscriber growth
7. Set up email campaigns
8. Send launch announcement

## Resources

- [Supabase Setup Guide](./SUPABASE_SETUP.md)
- [Deployment Guide](./DEPLOYMENT.md)
- [Quick Start Guide](./QUICKSTART.md)
- [Next.js Documentation](https://nextjs.org/docs)
- [Supabase Documentation](https://supabase.com/docs)

## Support

For questions or issues:
1. Check the troubleshooting section above
2. Review documentation files
3. Check browser console for errors
4. Review Supabase dashboard for data issues

---

**Your coming soon page is ready!** Set up Supabase and start collecting emails for your launch.
