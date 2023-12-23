import { ModeToggle } from "@/components/mode-toggle.tsx";
import FlashCard from "@/components/flashcard.tsx";

function Hexon() {
    return (
        <div className="bg-background flex flex-col justify-center items-center pt-20">
            <div className="w-full max-w-3xl mb-8 mx-auto p-6 bg-card rounded-md shadow relative">
                <div className="flex justify-between items-start">
                    <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
                        Hexon
                    </h1>
                    <ModeToggle/>
                </div>
                <p className="leading-7 [&:not(:first-child)]:mt-6">
                    Please select an option for what you'd like to learn.
                </p>
            </div>

            <FlashCard
                title="Sample Question"
                subtitle="Example Math Problem"
                description="What is 2 + 2?"
                answer="The answer is 4."
            />
        </div>
    )
}

export default Hexon;
