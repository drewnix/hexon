import type { NextPage } from 'next';
import Head from 'next/head';

const Board: NextPage = () => {
  return (
    <div className="container mx-auto">
      <Head>
        <title>Trivia</title>
        <meta name="description" content="Trivia" />
      </Head>
        <main className="py-0">
            <div className="bg-background flex flex-col justify-center items-center">
                <div className="w-full max-w-3xl mb-8 mx-auto p-6 bg-card rounded-md relative">
                    <h1>Trivia Board Goes Here!</h1>
                </div>
                </div>
        </main>
    </div>
);
};

export default Board;