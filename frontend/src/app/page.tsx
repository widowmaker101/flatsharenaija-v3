'use client';

import { useState } from 'react';
import { Hero, Input, Button } from 'daisyui';  // Note: DaisyUI components are used via classNames; import if needed for custom

export default function Home() {
  const [search, setSearch] = useState('');

  return (
    <div className="min-h-screen bg-base-200">
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="text-5xl font-bold">FlatShareNaija</h1>
            <p className="py-6">Find perfect flat shares in Nigeria with AI matching.</p>
            <div className="form-control">
              <Input 
                placeholder="Search locations, e.g., Lagos..." 
                value={search} 
                onChange={(e) => setSearch(e.target.value)} 
                className="input input-bordered w-full max-w-xs" 
              />
            </div>
            <Button className="btn btn-primary mt-4">Search</Button>
          </div>
        </div>
      </div>
    </div>
  );
}
