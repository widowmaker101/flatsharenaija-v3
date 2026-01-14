'use client';

import { useAuth } from '@/lib/AuthContext';

export default function MessagesPage() {
  const { token } = useAuth();

  if (!token) {
    return <div className="min-h-screen flex items-center justify-center">Please login to view messages.</div>;
  }

  return (
    <div className="min-h-screen bg-base-200 p-8">
      <h1 className="text-4xl font-bold text-center mb-8">Messages</h1>
      {/* Add chat UI here */}
      <p>Coming soon: Real-time messaging.</p>
    </div>
  );
}
