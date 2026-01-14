'use client';

import { useEffect, useState } from 'react';
import axios from 'axios';
import { Card, Button } from 'daisyui';

interface Match {
  candidate_id: number;
  score: number;
}

export default function MatchList({ userId }: { userId: number }) {
  const [matches, setMatches] = useState<Match[]>([]);
  const [token, setToken] = useState('');

  useEffect(() => {
    const storedToken = localStorage.getItem('token');
    if (storedToken) setToken(storedToken);
  }, []);

  useEffect(() => {
    if (token) {
      const fetchMatches = async () => {
        try {
          const response = await axios.get(`${process.env.API_URL}/matching/${userId}`, {
            headers: { Authorization: `Bearer ${token}` },
          });
          setMatches(response.data.matches);
        } catch (error) {
          console.error('Error fetching matches:', error);
        }
      };
      fetchMatches();
    }
  }, [token, userId]);

  return (
    <div className="space-y-4">
      {matches.map((match) => (
        <Card key={match.candidate_id} className="card bg-base-100 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">Candidate ID: {match.candidate_id}</h2>
            <p>Compatibility Score: {match.score}%</p>
            <div className="card-actions justify-end">
              <Button className="btn btn-primary">Message</Button>
            </div>
          </div>
        </Card>
      ))}
    </div>
  );
}
