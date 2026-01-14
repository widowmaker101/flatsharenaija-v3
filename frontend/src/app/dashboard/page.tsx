import { Button } from 'daisyui';
import Link from 'next/link';

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-base-200 p-8">
      <h1 className="text-4xl font-bold text-center mb-8">Dashboard</h1>
      <div className="flex flex-col items-center space-y-4">
        <Link href="/listings">
          <Button className="btn btn-primary w-64">View Listings</Button>
        </Link>
        <Link href="/matches">
<Link href="/messages">
  <Button className="btn btn-accent w-64">Messages</Button>
</Link>
          <Button className="btn btn-secondary w-64">Find Matches</Button>
        </Link>
        {/* Add more links/buttons as needed */}
      </div>
    </div>
  );
}
