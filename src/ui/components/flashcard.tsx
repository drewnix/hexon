// FlashCard.tsx
import {useState, useEffect} from 'react';
import { getFlashcard } from '@/apiService';


import {Button} from "@/components/ui/button"
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"

export interface FlashCardProps {
    topic: string;
}

interface Flashcard {
    title: string;
    description: string;
    answer: string;
    topic: string;
}

function FlashCard({ topic = 'All' }: FlashCardProps) {
    const [flashcard, setFlashcard] = useState<Flashcard | null>(null);
    const [isFlipped, setIsFlipped] = useState(false);
    const [isLoading, setIsLoading] = useState(false); // New state to track loading

    const fetchFlashcard = async () => {
        if (!topic) return; // Guard clause if topic is not provided
        setIsLoading(true); // Start loading

        try {
            const data = topic === "All"
                ? await getFlashcard()
                : await getFlashcard(topic)

            setIsFlipped(false); // Reset flip state here
            setFlashcard(data);
        } catch (error) {
            console.error('Error fetching flashcard:', error);
        } finally {
            setIsLoading(false); // End loading
        }
    };

    useEffect(() => {
        fetchFlashcard();
    }, [topic]); // Fetch a new card when the topic changes

    if (isLoading || !flashcard) {
        return <div>Loading...</div>;
    }

    const flipCard = () => {
        if (!isLoading) {
            setIsFlipped(!isFlipped);
        }
    };

    const handleNextClick = () => {
        fetchFlashcard(); // Fetch a new flashcard
    };

    if (!flashcard || isLoading) {
        return <div>Loading...</div>;
    }

    return (
        <Card className="w-full border-2 max-w-3xl mb-8 mx-auto p-6 bg-card rounded-md shadow relative">
            <CardHeader>
                <CardTitle>{flashcard.topic}</CardTitle>
                <CardDescription>{flashcard.title}</CardDescription>
            </CardHeader>
            <CardContent>
                <div className={`card-content ${isFlipped ? 'is-flipped' : ''}`}>
                    {/* Card Front */}
                    <div className="card-front rounded">
                        <p>{flashcard.description}</p>
                    </div>

                    {/* Card Back */}
                    <div className="card-back rounded">
                        <p>{flashcard.answer}</p>
                    </div>
                </div>

                <CardFooter className="flex justify-between">
                    <Button onClick={handleNextClick} className="w-20 rounded p-4">Next</Button>
                    <Button onClick={flipCard} className="w-20 rounded p-4">Flip</Button>
                </CardFooter>
            </CardContent>
        </Card>
    );
}

export default FlashCard;
