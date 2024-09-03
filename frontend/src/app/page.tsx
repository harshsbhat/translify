'use client';

import { useEffect, useState } from 'react';
import { Button } from '@/components/ui/button';
import { CopyButton } from '@/components/ui/copy';
import Link from 'next/link';
import { Tabs, TabsList, TabsTrigger, TabsContent } from '@/components/ui/tabs';

export default function Home() {
  const [count, setCount] = useState<string | null>(null);

  useEffect(() => {
    async function fetchCount() {
      try {
        const response = await fetch('/api/getCount');
        const data = await response.json();
        setCount(data.count);
      } catch (error) {
        console.error('Error fetching count:', error);
      }
    }

    fetchCount();
  }, []);

  const curlCommand = `
curl -X POST http://127.0.0.1:5000/translate \\
  -H "Content-Type: application/json" \\
  -d '{
      "url": "https://firecrawl.dev",
      "action": "scrape"
    }'
  `;


  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <Button variant="outline" className="rounded-full mb-7 text-sm p-5 text-zinc-400">
        <Link href="https://github.com/mendableai/firecrawl" passHref
            target="_blank"
            rel="noopener noreferrer"
            className="text-zinc-400 hover:text-zinc-300"
          >
            Star Firecrawl on&nbsp;<span className="text-zinc-200">Github ⭐</span>
        </Link>
      </Button>
      <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-6xl bg-gradient-to-b from-zinc-200 to-zinc-400 text-transparent bg-clip-text text-center">
        ENGLISH or SPANISH
      </h1>
      <p className="text-zinc-500 leading-7 [&:not(:first-child)]:mt-6 text-center">

Easily convert web content to Spanish with our API. Just input a URL, choose scrape or crawl, and let our API handle the translation. <br /> Quick, accurate, and user-friendly.
      </p>

      <Tabs defaultValue="curl" className="w-full max-w-5xl mt-10">
        <TabsList>
          <TabsTrigger value="curl">cURL</TabsTrigger>
        </TabsList>
        <TabsContent value="curl">
          <div className="bg-zinc-900 text-zinc-400 p-6 rounded-lg relative">
            <pre>
              <code>{curlCommand}</code>
            </pre>
            <CopyButton text={curlCommand} />
          </div>
        </TabsContent>
      </Tabs>

    </main>
  );
}