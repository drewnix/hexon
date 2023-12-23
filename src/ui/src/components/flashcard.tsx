// FlashCard.tsx
import {useState} from 'react';

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
    title: string;
    subtitle: string;
    description: string;
    answer: string;
}

function FlashCard({title, subtitle, description, answer}: FlashCardProps) {
    const [isFlipped, setIsFlipped] = useState(false);

    const flipCard = () => setIsFlipped(!isFlipped);

    return (
        <Card className="w-full max-w-3xl mb-8 mx-auto p-6 bg-card rounded-md shadow relative">
            <CardHeader>
                <CardTitle>{title}</CardTitle>
                <CardDescription>{subtitle}</CardDescription>
            </CardHeader>
            <CardContent>
                <div className={`card-content ${isFlipped ? 'is-flipped' : ''}`}>
                    {/* Card Front */}
                    <div className="card-front rounded">
                        <p>{description}</p>
                    </div>

                    {/* Card Back */}
                    <div className="card-back rounded">
                        <p>{answer}</p>
                    </div>
                </div>

                <CardFooter className="flex justify-between">
                    <Button className="rounded p-4">Next</Button>
                    <Button onClick={flipCard} className="rounded p-4">Flip</Button>
                </CardFooter>
            </CardContent>
        </Card>
    );
}

export default FlashCard;
