'use client';

import { useState } from 'react';  // Assume userId from context or props; hardcoded for example
import MatchList from '@/components/MatchList';

export default function MatchesPage() {
  const userId = 1;  // Replace with actual user ID from auth context

  return (
    <div className="min-h-screen bg-base-200 p-8">
      <h1 className="text-4xl font-bold text-center mb-8">AI Roommate Matches</h1>
      <MatchList userId={userId} />
    </div>
  );
}
