import os
from google import genai
from dotenv import load_dotenv

# Load env variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("WARNING: GOOGLE_API_KEY not found in environment variables.")

# Configure the library
client = genai.Client(api_key=API_KEY)

def query_gemini(prompt, system_instruction=None, model_name="gemini-3-flash-preview", response_schema=None):
    """
    Sends a prompt to Gemini and returns the text response.
    Supports structured output if response_schema is provided.
    """
    try:
        if system_instruction:
            # Native system instruction support if available in this client version, 
            # but sticking to prompt prepend for safety unless we see config options.
            # actually, let's stick to prompt prepending for now as it worked, 
            # BUT if we use response_schema, ensure it's compatible.
            final_prompt = f"System Instruction: {system_instruction}\n\nUser Prompt: {prompt}"
        else:
            final_prompt = prompt

        config = {}
        if response_schema:
            config = {
                "response_mime_type": "application/json",
                "response_json_schema": response_schema
            }

        response = client.models.generate_content(
            model=model_name,
            contents=final_prompt,
            config=config if config else None
        )
        
        return response.text

    except Exception as e:
        return f"Error querying Gemini: {str(e)}"
