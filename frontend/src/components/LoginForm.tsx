'use client';

import { useState } from 'react';
import axios from 'axios';
import { Input, Button, Card } from 'daisyui';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async () => {
    try {
      const response = await axios.post(`${process.env.API_URL}/users/login`, {
        username: email,
        password,
      }, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      });
      localStorage.setItem('token', response.data.access_token);
      const { setToken, setUserId } = useAuth(); setToken(response.data.access_token); // Fetch/set userId
      // Redirect or update state
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  return (
    <Card className="card w-96 bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">Login</h2>
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
        <Button onClick={handleSubmit} className="btn btn-primary">Login</Button>
      </div>
    </Card>
  );
}
