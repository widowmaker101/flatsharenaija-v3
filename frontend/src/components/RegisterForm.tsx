'use client';

import { useState } from 'react';
import axios from 'axios';
import { Input, Button, Card } from 'daisyui';

export default function RegisterForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [preferences, setPreferences] = useState({});  // Example: {lifestyle: 'quiet', budget: 50000}

  const handleSubmit = async () => {
    try {
      const response = await axios.post(`${process.env.API_URL}/users/`, {
        email,
        password,
        preferences,
      });
      console.log('Registered:', response.data);
      // Handle success, e.g., redirect or store token if returned
    } catch (error) {
      console.error('Registration error:', error);
    }
  };

  return (
    <Card className="card w-96 bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">Register</h2>
        <Input 
          placeholder="Email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
          className="input input-bordered" 
        />
        <Input 
          type="password" 
          placeholder="Password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
          className="input input-bordered" 
        />
        {/* Add inputs for preferences as needed */}
        <Button onClick={handleSubmit} className="btn btn-primary">Sign Up</Button>
      </div>
    </Card>
  );
}
