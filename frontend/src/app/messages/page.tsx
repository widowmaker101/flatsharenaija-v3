'use client';

import { useEffect, useState } from 'react';
import io from 'socket.io-client';
import { useAuth } from '@/lib/AuthContext';
import { Input, Button, Card } from 'daisyui';

const socket = io(process.env.API_URL || 'http://localhost:8000');

export default function MessagesPage() {
  const { token } = useAuth();
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState<string[]>([]);

  useEffect(() => {
    if (token) {
      socket.on('connect', () => console.log('Connected to socket'));
      socket.on('message', (msg) => setMessages((prev) => [...prev, msg]));
    }
    return () => {
      socket.off('message');
    };
  }, [token]);

  const sendMessage = () => {
    if (message) {
      socket.emit('message', message);
      setMessage('');
    }
  };

  if (!token) {
    return <div className="min-h-screen flex items-center justify-center">Please login to view messages.</div>;
  }

  return (
    <div className="min-h-screen bg-base-200 p-8">
      <h1 className="text-4xl font-bold text-center mb-8">Messages</h1>
      <Card className="card bg-base-100 shadow-xl mb-4">
        <div className="card-body">
          {messages.map((msg, idx) => (
            <p key={idx}>{msg}</p>
          ))}
        </div>
      </Card>
      <div className="form-control flex-row">
        <Input 
          placeholder="Type a message..." 
          value={message} 
          onChange={(e) => setMessage(e.target.value)} 
          className="input input-bordered flex-1 mr-2" 
        />
        <Button onClick={sendMessage} className="btn btn-primary">Send</Button>
      </div>
    </div>
  );
}
