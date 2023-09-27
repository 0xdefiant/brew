import os
import openai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Retrieve the API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/get-recipe', methods=['POST'])
def get_recipe():
    ingredients = request.json.get('ingredients', [])

    # Convert list of ingredients to a string for the prompt
    ingredients_str = ", ".join(ingredients)

    message = {
        "role": "system",
        "content": "You are a helpful assistant that provides beer recipes based on available ingredients."
    }
    user_message = {
        "role": "user",
        "content": f"I have the following ingredients: {ingredients_str}. What's a potential beer recipe I can make with these?"
    }

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[message, user_message]
    )

    # Get the AI's response
    ai_response = response.choices[0].message['content']

    return jsonify({"suggestion": ai_response})


if __name__ == '__main__':
    app.run(port=5000)
