'use server';

import { supabase } from '@/lib/supabase';

interface SubscribeData {
  username: string;
  email: string;
}

export async function subscribeUser(data: SubscribeData) {
  try {
    // Validate input
    if (!data.username || !data.email) {
      return {
        success: false,
        error: 'Username and email are required',
      };
    }

    // Simple email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
      return {
        success: false,
        error: 'Please enter a valid email address',
      };
    }

    // Check if email already exists
    const { data: existingUser } = await supabase
      .from('subscribers')
      .select('email')
      .eq('email', data.email)
      .single();

    if (existingUser) {
      return {
        success: false,
        error: 'This email is already subscribed',
      };
    }

    // Insert into database
    const { data: result, error } = await supabase
      .from('subscribers')
      .insert([
        {
          username: data.username,
          email: data.email,
          created_at: new Date(),
        },
      ])
      .select();

    if (error) {
      console.error('Supabase error:', error);
      return {
        success: false,
        error: 'Failed to subscribe. Please try again.',
      };
    }

    return {
      success: true,
      message: 'Successfully subscribed! Check your email for updates.',
      data: result,
    };
  } catch (error) {
    console.error('Subscribe error:', error);
    return {
      success: false,
      error: 'An unexpected error occurred',
    };
  }
}
