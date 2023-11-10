# brew
# Beer Recipe Assistant

## Overview
This Python application is a personal project developed for my dad, who recently retired and started to brew beer as a hobby. I created this basic script to help him easily generate beer recipes using the ingredients he has on hand. It leverages OpenAI to suggest creative and practical beer recipes.

## Features
- **Web Interface**: A simple Flask web application where users can input their available ingredients.
- **AI-Powered Recipe Suggestions**: Utilizes OpenAI to generate beer recipes based on the given ingredients.

## How It Works
1. **Home Page**: The user is presented with a form to enter the ingredients they have.
2. **Recipe Generation**: After submitting the ingredients, the AI model processes them and returns a potential beer recipe.

## Technologies Used
- Python: For backend logic.
- Flask: To create the web interface.
- OpenAI API: For generating AI-based responses.
- dotenv: For managing environment variables.

## Setup and Installation
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```
   pip install flask openai python-dotenv
   ```
3. Set up an `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```
   python app.py
   ```

## Usage
1. Open the web application.
2. Enter the ingredients available for brewing in the provided form.
3. Submit the form to receive a beer recipe suggestion from the AI.

## Motivation
The inspiration behind this project is my father, who started homebrewing after retirement. I wanted to create a tool that simplifies the process of finding new and exciting beer recipes for him.

## Future Enhancements
- Expand the recipe database to include more diverse brewing methods and ingredients.
- Implement a feature to adjust recipes based on the quantity of ingredients available.
- Integrate user feedback to improve the AI's recipe suggestions.
