import FlashCard from '../components/flashcard';
import {ThemeProvider} from "@/components/theme-provider"
import type { Meta } from '@storybook/react';


const meta: Meta<typeof FlashCard> = {
  title: 'drewnix.dev/FlashCard',
  component: FlashCard,
};

export default meta;

// Named export for each story
export const Default = () => (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
        <FlashCard
            topic={"Literature"}
        />
    </ThemeProvider>
);

export const Mathematics = () => (
    <FlashCard
        topic={"Mathematics"}
    />
);

export const Geography = () => (
    <FlashCard
        topic={"Geography"}
    />
);

export const Politics = () => (
    <FlashCard
        topic={"Politics"}
    />
);
