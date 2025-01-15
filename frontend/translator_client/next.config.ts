import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: "http://django:8000/api/:path*",
      },
    ];
  },
};

export default nextConfig;
