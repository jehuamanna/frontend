# Supabase Setup Guide

This guide will walk you through setting up Supabase to collect email subscriptions for your coming soon page.

## Step 1: Create a Supabase Account

1. Visit [supabase.com](https://supabase.com)
2. Click "Sign Up" and create an account
3. You can sign up with Email, GitHub, Google, or GitLab

## Step 2: Create a New Project

1. After logging in, click "New Project"
2. Enter a project name (e.g., "Frontend System Design")
3. Set a secure database password
4. Select your region (choose the one closest to your users)
5. Click "Create new project"

Wait for the project to initialize (this may take a few minutes).

## Step 3: Create the Subscribers Table

Once your project is ready:

1. Go to the "SQL Editor" in the sidebar
2. Click "New Query"
3. Copy and paste this SQL code:

```sql
CREATE TABLE subscribers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Create an index on email for faster lookups
CREATE INDEX idx_subscribers_email ON subscribers(email);

-- Enable Row Level Security (RLS)
ALTER TABLE subscribers ENABLE ROW LEVEL SECURITY;

-- Allow anyone to insert new subscribers
CREATE POLICY "Anyone can insert subscribers" ON subscribers
  FOR INSERT WITH CHECK (true);

-- Allow anyone to read subscribers (optional)
CREATE POLICY "Anyone can read subscribers" ON subscribers
  FOR SELECT USING (true);
```

4. Click "Run" or press Ctrl+Enter
5. You should see "Success" message

## Step 4: Get Your API Keys

1. In the sidebar, go to "Project Settings" (gear icon)
2. Click on "API" in the menu
3. You'll see your project URL and API keys

You need two values:
- **Project URL**: Copy this (format: https://xxxxx.supabase.co)
- **anon key**: Copy this from the "anon public" section

## Step 5: Set Environment Variables

1. In your project root, create a `.env.local` file (this is not tracked by git)
2. Add these lines:

```
NEXT_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
```

Replace the values with your actual Project URL and anon key.

**Important:** These are public keys (hence the `NEXT_PUBLIC_` prefix), so they're safe to expose in the frontend.

## Step 6: Test the Setup

1. Start your development server:
```bash
npm run dev
```

2. Visit `http://localhost:3000`

3. You should see the subscription form on the hero section

4. Try submitting with a test email (e.g., test@example.com)

5. If successful, you'll see a success message

## Step 7: Verify Data in Supabase

1. Go back to your Supabase dashboard
2. Click on "Table Editor" in the sidebar
3. Select the "subscribers" table
4. You should see your test subscription with the username and email

## Monitoring Subscribers

### View All Subscribers
1. In Supabase dashboard, go to "Table Editor"
2. Click on "subscribers" table
3. You can view, edit, or delete entries here

### Export Subscribers
1. In the subscribers table, click the three dots menu
2. Select "Download as CSV"
3. This exports all subscriber data

### Set up Email Notifications (Optional)

Supabase supports webhooks to trigger actions when data changes:

1. Go to "Database" -> "Webhooks"
2. Click "Create a new webhook"
3. Configure it to send you an email when new subscribers join

## Troubleshooting

### "Missing Supabase environment variables" error
- Make sure you created the `.env.local` file
- Verify you copied the correct URL and anon key
- Restart the development server after adding environment variables

### "Failed to subscribe" error
- Check the browser console for detailed error messages
- Verify the subscribers table exists in Supabase
- Check that RLS policies are set correctly

### Duplicate email error
- The system prevents the same email from subscribing twice
- This is working as intended

### Network errors
- Make sure your Supabase project is active
- Check your internet connection
- Verify the project URL is correct

## Security Notes

1. The `NEXT_PUBLIC_*` variables are public and visible in the frontend code
2. Never put secrets in `NEXT_PUBLIC_*` variables
3. Supabase RLS policies control what data can be accessed
4. The anon key is restricted by RLS, so it can only insert subscribers

## Advanced: Custom Domain Email (Optional)

To set up automated emails when users subscribe:

1. Install Supabase CLI: `npm install -g supabase`
2. Set up email templates in Supabase
3. Use edge functions to send emails
4. See [Supabase docs](https://supabase.com/docs/guides/realtime) for details

## Scaling Considerations

- Supabase handles thousands of subscribers easily
- Standard tier supports unlimited API calls
- Use the Table Editor to manage data
- Consider setting up backups through Supabase UI

## Next Steps

1. Customize the form styling in `app/components/SubscriptionForm.tsx`
2. Add your brand colors and fonts
3. Customize success/error messages
4. Set up email campaigns for subscribers
5. Monitor subscriber growth

## Resources

- [Supabase Documentation](https://supabase.com/docs)
- [Supabase Dashboard](https://app.supabase.com)
- [SQL Tutorial](https://supabase.com/docs/guides/database)
- [API Reference](https://supabase.com/docs/reference)

---

**Your subscription form is now ready!** Users can subscribe and their data will be safely stored in Supabase.
