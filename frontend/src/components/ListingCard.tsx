import { Card, Button } from 'daisyui';

interface ListingProps {
  location: string;
  price_ngn: number;
  amenities: string[];
  description?: string;
}

export default function ListingCard({ location, price_ngn, amenities, description }: ListingProps) {
  return (
    <Card className="card bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">{location} - ₦{price_ngn}</h2>
        <p>{description}</p>
        <div className="badge-container">
          {amenities.map((amenity, index) => (
            <span key={index} className="badge badge-secondary mr-1">{amenity}</span>
          ))}
        </div>
        <div className="card-actions justify-end">
          <Button className="btn btn-primary">Contact</Button>
        </div>
      </div>
    </Card>
  );
}
