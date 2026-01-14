import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  env: {
    API_URL: 'http://localhost:8000',
    COUNTRY: 'ng',
  },
};
export default nextConfig;
