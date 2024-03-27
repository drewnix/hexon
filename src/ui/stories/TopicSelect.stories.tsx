import { useState } from 'react';
import {TopicSelect} from '../components/topic-select';
import {ThemeProvider} from "@/components/theme-provider"
import type { Meta } from '@storybook/react';


const meta: Meta<typeof TopicSelect> = {
  title: 'drewnix.dev/TopicSelect',
  component: TopicSelect,
};

export default meta;

interface TopicSelectProps {
  selectedTopic: string;
  setSelectedTopic: (topic: string) => void;
}

const Template = (args: TopicSelectProps) => {
  const [selectedTopic, setSelectedTopic] = useState("");

  return (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
      <TopicSelect {...args} selectedTopic={selectedTopic} setSelectedTopic={setSelectedTopic} />
    </ThemeProvider>
  );
};

export const Default = Template.bind({});
