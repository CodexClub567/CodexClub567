import openai
import os
# Optional import for Gemini
# import google.generativeai as genai

def generate_script(openai_key, gemini_key, topic): # Added gemini_key
    """
    Generates a script using OpenAI and optionally Gemini.

    Args:
        openai_key: OpenAI API key.
        gemini_key: Google Gemini API key (optional).
        topic: The topic of the script.

    Returns:
        The generated script, or None on error.
    """
    openai.api_key = openai_key

    # Use a try-except block to handle potential errors
    try:
        # Attempt to use Gemini if available and a key is provided
        if gemini_key:
            # genai.configure(api_key=gemini_key) #removed os.getenv
            # model = genai.GenerativeModel("gemini-pro") #removed hardcoded model
            # response = model.generate_content(f"Write a script about {topic}")
            # return response.text
            return "Gemini script generation is a placeholder." # Placeholder

        else:
            # Fallback to OpenAI
            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",  # Specify the model
                prompt=f"Write a detailed script about {topic} for a YouTube video, with clear chapters and engaging content.",
                max_tokens=1000,  # Adjust as needed
            )
            return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating script: {e}")
        return None
