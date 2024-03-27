import type { NextPage } from 'next';
import Head from 'next/head';
import TriviaGPT from '@/components/triviagpt'

const Home: NextPage = () => {
  return (
    <div className="container mx-auto">
      <Head>
        <title>Trivia</title>
        <meta name="description" content="Trivia" />
      </Head>
      <main className="py-0">
          <TriviaGPT/>
      </main>
    </div>
  );
};

export default Home;