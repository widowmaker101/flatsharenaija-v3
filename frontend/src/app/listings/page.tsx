'use client';

import { useEffect, useState } from 'react';
import axios from 'axios';
import ListingCard from '@/components/ListingCard';

interface Listing {
  id: number;
  location: string;
  price_ngn: number;
  amenities: string[];
  description?: string;
}

export default function ListingsPage() {
  const [listings, setListings] = useState<Listing[]>([]);
  const [token, setToken] = useState('');

  useEffect(() => {
    const storedToken = localStorage.getItem('token');
    if (storedToken) setToken(storedToken);
  }, []);

  useEffect(() => {
    if (token) {
      const fetchListings = async () => {
        try {
          const response = await axios.get(`${process.env.API_URL}/listings`, {
            headers: { Authorization: `Bearer ${token}` },
          });
          setListings(response.data);
        } catch (error) {
          console.error('Error fetching listings:', error);
        }
      };
      fetchListings();
    }
  }, [token]);

  return (
    <div className="min-h-screen bg-base-200 p-8">
      <h1 className="text-4xl font-bold text-center mb-8">Available Listings</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {listings.map((listing) => (
          <ListingCard 
            key={listing.id}
            location={listing.location}
            price_ngn={listing.price_ngn}
            amenities={listing.amenities}
            description={listing.description}
          />
        ))}
      </div>
    </div>
  );
}
