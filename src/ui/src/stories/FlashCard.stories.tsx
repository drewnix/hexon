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
            topic="Hodgepodge"
        />
    </ThemeProvider>
);

export const Mathematics = () => (
    <FlashCard
        topic="Problems"
    />
);

export const Geography = () => (
    <FlashCard
        topic={"Geography"}
    />
);

export const History = () => (
    <FlashCard
        topic="US Presidents"
    />
);
