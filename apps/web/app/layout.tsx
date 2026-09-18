import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Nexus AI",
  description: "Agentic Enterprise Research & Knowledge System",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}