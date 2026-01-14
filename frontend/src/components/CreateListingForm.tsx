'use client';

import { useState } from 'react';
import axios from 'axios';
import { Input, Button, Card, Textarea } from 'daisyui';
import { useAuth } from '@/lib/AuthContext';

export default function CreateListingForm() {
  const { token, userId } = useAuth();
  const [location, setLocation] = useState('');
  const [price, setPrice] = useState(0);
  const [amenities, setAmenities] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async () => {
    if (!token || !userId) return;
    try {
      await axios.post(`${process.env.API_URL}/listings/`, {
        location,
        price_ngn: price,
        amenities: amenities.split(','),
        description,
      }, {
        headers: { Authorization: `Bearer ${token}` },
        params: { user_id: userId },  // Pass user_id if needed
      });
      alert('Listing created!');
    } catch (error) {
      console.error('Error creating listing:', error);
    }
  };

  return (
    <Card className="card w-96 bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">Create Listing</h2>
        <Input placeholder="Location e.g., Lagos" value={location} onChange={(e) => setLocation(e.target.value)} />
        <Input type="number" placeholder="Price (NGN)" value={price} onChange={(e) => setPrice(parseFloat(e.target.value))} />
        <Input placeholder="Amenities (comma-separated)" value={amenities} onChange={(e) => setAmenities(e.target.value)} />
        <Textarea placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
        <Button onClick={handleSubmit} className="btn btn-primary">Post Listing</Button>
      </div>
    </Card>
  );
}
