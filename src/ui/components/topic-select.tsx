"use client"

import * as React from "react"
import {Check, ChevronsUpDown} from "lucide-react"
import {getTopics} from '../apiService';

import {cn} from "@/lib/utils"
import {Button} from "@/components/ui/button"
import {
    Command,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
} from "@/components/ui/command"
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover"
import {useEffect, useState} from "react";

interface TopicSelectProps {
  selectedTopic: string;
  setSelectedTopic: (topic: string) => void;
}

export function TopicSelect({ selectedTopic, setSelectedTopic }: TopicSelectProps) {

    const [open, setOpen] = useState(false)
    const [isLoading, setIsLoading] = useState(false); // New state to track loading
    const [topics, setTopics] = useState(['All'])

    const fetchTopics = async () => {
        setIsLoading(true); // Start loading

        try {
            const data = await getTopics();
            setTopics(['All', ...data]);
        } catch (error) {
            console.error('Error fetching flashcard:', error);
        } finally {
            setIsLoading(false); // End loading
        }
    };

    useEffect(() => {
        fetchTopics();
    }, []);

    return (
        <Popover open={open} onOpenChange={setOpen}>
            <PopoverTrigger asChild>
                <Button
                    variant="outline"
                    role="combobox"
                    aria-expanded={open}
                    className="w-[200px] justify-between"
                >
                    {selectedTopic || "Select topic..."}
                    <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50"/>
                </Button>
            </PopoverTrigger>
            <PopoverContent className="w-[200px] p-0">
                <Command>
                    <CommandInput placeholder="Select Topic ..."/>
                    {isLoading ? (
                        <CommandEmpty>Loading topics...</CommandEmpty>
                    ) : topics.length > 0 ? (
                        <CommandGroup>
                            {topics.map((topic, index) => (
                                <CommandItem
                                    key={index}
                                    onSelect={() => {
                                        // setValue(topic === value ? "" : topic);
                                        setSelectedTopic(topic === selectedTopic ? "" : topic);
                                        setOpen(false);
                                    }}
                                >
                                    <Check
                                        className={cn(
                                            "mr-2 h-4 w-4",
                                             selectedTopic === topic ? "opacity-100" : "opacity-0"
                                        )}
                                    />
                                    {topic}
                                </CommandItem>
                            ))}
                        </CommandGroup>
                    ) : (
                        <CommandEmpty>No topics found.</CommandEmpty>
                    )}
                </Command>
            </PopoverContent>
        </Popover>
    )
}
