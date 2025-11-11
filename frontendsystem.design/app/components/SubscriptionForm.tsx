'use client';

import { useState, useEffect } from 'react';
import { subscribeUser } from '@/app/actions/subscribe';

interface FormErrors {
  username?: string;
  email?: string;
}

export default function SubscriptionForm() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
  });
  const [errors, setErrors] = useState<FormErrors>({});
  const [isLoading, setIsLoading] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<{
    type: 'success' | 'error' | null;
    message: string;
  }>({ type: null, message: '' });
  const [touched, setTouched] = useState({
    username: false,
    email: false,
  });

  // Client-side validation
  const validateField = (name: string, value: string): string | undefined => {
    switch (name) {
      case 'username':
        if (!value.trim()) {
          return 'Username is required';
        }
        if (value.length < 3) {
          return 'Username must be at least 3 characters';
        }
        if (value.length > 30) {
          return 'Username must be less than 30 characters';
        }
        return undefined;

      case 'email':
        if (!value.trim()) {
          return 'Email is required';
        }
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
          return 'Please enter a valid email address';
        }
        return undefined;

      default:
        return undefined;
    }
  };

  // Validate form on change
  useEffect(() => {
    const newErrors: FormErrors = {};
    
    if (touched.username) {
      const usernameError = validateField('username', formData.username);
      if (usernameError) newErrors.username = usernameError;
    }
    
    if (touched.email) {
      const emailError = validateField('email', formData.email);
      if (emailError) newErrors.email = emailError;
    }

    setErrors(newErrors);
  }, [formData, touched]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    // Clear submit status when user starts typing again
    if (submitStatus.type) {
      setSubmitStatus({ type: null, message: '' });
    }
  };

  const handleBlur = (e: React.FocusEvent<HTMLInputElement>) => {
    const { name } = e.target;
    setTouched(prev => ({ ...prev, [name]: true }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Mark all fields as touched
    setTouched({ username: true, email: true });

    // Validate all fields
    const usernameError = validateField('username', formData.username);
    const emailError = validateField('email', formData.email);

    if (usernameError || emailError) {
      setErrors({
        username: usernameError,
        email: emailError,
      });
      return;
    }

    // Submit form
    setIsLoading(true);
    setSubmitStatus({ type: null, message: '' });

    try {
      const result = await subscribeUser(formData);

      if (result.success) {
        setSubmitStatus({
          type: 'success',
          message: result.message || 'Successfully subscribed!',
        });
        // Reset form
        setFormData({ username: '', email: '' });
        setTouched({ username: false, email: false });
        setErrors({});
      } else {
        setSubmitStatus({
          type: 'error',
          message: result.error || 'Something went wrong. Please try again.',
        });
      }
    } catch (error) {
      setSubmitStatus({
        type: 'error',
        message: 'An unexpected error occurred. Please try again.',
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="w-full max-w-md mx-auto">
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Username Field */}
        <div className="space-y-2">
          <label
            htmlFor="username"
            className="block text-sm font-medium text-gray-700 dark:text-gray-300"
          >
            Username
          </label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            onBlur={handleBlur}
            disabled={isLoading}
            className={`w-full px-4 py-3 rounded-lg border-2 transition-all duration-200
              bg-white dark:bg-gray-800 
              text-gray-900 dark:text-gray-100
              placeholder-gray-400 dark:placeholder-gray-500
              focus:outline-none focus:ring-2 focus:ring-offset-2
              disabled:opacity-50 disabled:cursor-not-allowed
              ${
                errors.username && touched.username
                  ? 'border-red-500 focus:ring-red-500'
                  : !errors.username && touched.username && formData.username
                  ? 'border-green-500 focus:ring-green-500'
                  : 'border-gray-300 dark:border-gray-600 focus:ring-blue-500'
              }`}
            placeholder="Enter your username"
            aria-invalid={errors.username && touched.username ? 'true' : 'false'}
            aria-describedby={errors.username ? 'username-error' : undefined}
          />
          {errors.username && touched.username && (
            <p
              id="username-error"
              className="text-sm text-red-600 dark:text-red-400 animate-in fade-in duration-200"
            >
              {errors.username}
            </p>
          )}
          {!errors.username && touched.username && formData.username && (
            <p className="text-sm text-green-600 dark:text-green-400 animate-in fade-in duration-200">
              ✓ Looks good!
            </p>
          )}
        </div>

        {/* Email Field */}
        <div className="space-y-2">
          <label
            htmlFor="email"
            className="block text-sm font-medium text-gray-700 dark:text-gray-300"
          >
            Email
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            onBlur={handleBlur}
            disabled={isLoading}
            className={`w-full px-4 py-3 rounded-lg border-2 transition-all duration-200
              bg-white dark:bg-gray-800 
              text-gray-900 dark:text-gray-100
              placeholder-gray-400 dark:placeholder-gray-500
              focus:outline-none focus:ring-2 focus:ring-offset-2
              disabled:opacity-50 disabled:cursor-not-allowed
              ${
                errors.email && touched.email
                  ? 'border-red-500 focus:ring-red-500'
                  : !errors.email && touched.email && formData.email
                  ? 'border-green-500 focus:ring-green-500'
                  : 'border-gray-300 dark:border-gray-600 focus:ring-blue-500'
              }`}
            placeholder="Enter your email"
            aria-invalid={errors.email && touched.email ? 'true' : 'false'}
            aria-describedby={errors.email ? 'email-error' : undefined}
          />
          {errors.email && touched.email && (
            <p
              id="email-error"
              className="text-sm text-red-600 dark:text-red-400 animate-in fade-in duration-200"
            >
              {errors.email}
            </p>
          )}
          {!errors.email && touched.email && formData.email && (
            <p className="text-sm text-green-600 dark:text-green-400 animate-in fade-in duration-200">
              ✓ Looks good!
            </p>
          )}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={isLoading || Object.keys(errors).length > 0}
          className="w-full px-6 py-3 rounded-lg font-semibold text-white
            bg-gradient-to-r from-blue-600 to-purple-600
            hover:from-blue-700 hover:to-purple-700
            focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
            disabled:opacity-50 disabled:cursor-not-allowed
            transform transition-all duration-200
            hover:scale-[1.02] active:scale-[0.98]
            shadow-lg hover:shadow-xl"
        >
          {isLoading ? (
            <span className="flex items-center justify-center gap-2">
              <svg
                className="animate-spin h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                />
              </svg>
              Subscribing...
            </span>
          ) : (
            'Subscribe to Newsletter'
          )}
        </button>

        {/* Success/Error Messages */}
        {submitStatus.type && (
          <div
            className={`p-4 rounded-lg animate-in fade-in slide-in-from-top-2 duration-300 ${
              submitStatus.type === 'success'
                ? 'bg-green-50 dark:bg-green-900/20 border-2 border-green-500 text-green-800 dark:text-green-300'
                : 'bg-red-50 dark:bg-red-900/20 border-2 border-red-500 text-red-800 dark:text-red-300'
            }`}
            role="alert"
          >
            <div className="flex items-start gap-3">
              {submitStatus.type === 'success' ? (
                <svg
                  className="w-5 h-5 mt-0.5 flex-shrink-0"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    fillRule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clipRule="evenodd"
                  />
                </svg>
              ) : (
                <svg
                  className="w-5 h-5 mt-0.5 flex-shrink-0"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    fillRule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                    clipRule="evenodd"
                  />
                </svg>
              )}
              <p className="text-sm font-medium">{submitStatus.message}</p>
            </div>
          </div>
        )}
      </form>
    </div>
  );
}