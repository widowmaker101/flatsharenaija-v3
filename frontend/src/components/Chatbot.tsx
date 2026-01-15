'use client';

import { useState } from 'react';
import axios from 'axios';
import { Input, Button, Card } from 'daisyui';

export default function Chatbot() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleQuery = async () => {
    try {
      const res = await axios.post(`${process.env.API_URL}/chat`, { message: query });
      setResponse(res.data.response);
    } catch (error) {
      console.error('Chatbot error:', error);
    }
  };

  return (
    <Card className="fixed bottom-4 right-4 w-80 bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">AI Support</h2>
        <Input placeholder="Ask anything..." value={query} onChange={(e) => setQuery(e.target.value)} />
        <Button onClick={handleQuery} className="btn btn-primary">Send</Button>
        <p>{response}</p>
      </div>
    </Card>
  );
}
