// src/services/apiService.js

const BASE_URL = 'http://localhost:8000/api'; // Adjust this to your API's URL

const getFlashcard = async (topic: string) => {
    try {
        const response = await fetch(`${BASE_URL}/card/?topic=${encodeURIComponent(topic)}`)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching flashcard:', error);
        // Handle errors as appropriate for your application
    }
};

export { getFlashcard };
