'use client';

import { useEffect, useState } from 'react';
import SubscriptionForm from '@/app/components/SubscriptionForm';

export default function Home() {
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    setIsLoaded(true);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-blue-50 to-teal-50 flex items-center justify-center px-4 py-8">
      <style>{`
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        
        .fade-in {
          animation: fadeIn 1.2s ease-out forwards;
        }
        
        .gradient-text {
          background: linear-gradient(to right, #14B8A6, #2563EB, #14B8A6);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
        }
      `}</style>

      <div className="flex flex-col items-center justify-center gap-12">
        {/* Main heading */}
        <div className={isLoaded ? 'fade-in' : 'opacity-0'}>
          <div className="text-center">
            <h1 className="text-6xl md:text-7xl lg:text-8xl font-black text-slate-900 leading-tight tracking-tight">
              HELLO
            </h1>
            <h2 className="text-6xl md:text-7xl lg:text-8xl font-black leading-tight tracking-tight mt-4 gradient-text">
              Frontend System Design
            </h2>
          </div>
          
        </div>

        {/* Subscription Form */}
        <div className={isLoaded ? 'fade-in' : 'opacity-0'} style={{ animationDelay: '0.3s' }}>
          <SubscriptionForm />
        </div>
      </div>
    </div>
  );
}
