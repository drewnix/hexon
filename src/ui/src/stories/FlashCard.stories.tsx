import FlashCard from '../components/flashcard';
import {ThemeProvider} from "@/components/theme-provider"
import type { Meta } from '@storybook/react';


const meta: Meta<typeof FlashCard> = {
  component: FlashCard,
};

export default meta;

// Named export for each story
export const Default = () => (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
        <FlashCard
            title="Sample Question"
            topic="Hodgepodge"
            description="What is 2 + 2?"
            answer="The answer is 4."
        />
    </ThemeProvider>
);

export const Mathematics = () => (
    <FlashCard
        title="Math Question"
        topic="Problems"
        description="What is the square root of 16?"
        answer="The answer is 4."
    />
);

export const Geography = () => (
    <FlashCard
        title="Geography Question"
        topic={"Country capitals"}
        description="What is the capital of France?"
        answer="The answer is Paris."
    />
);

export const History = () => (
    <FlashCard
        title="History Question"
        topic="US Presidents"
        description="Who was the first President of the United States?"
        answer="The answer is George Washington."
    />
);
