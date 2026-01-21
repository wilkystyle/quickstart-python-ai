from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

if __name__ == "__main__":
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents={"text": "Please write a haiku about computers"},
        config={
            "temperature": 1.0,  # 0.0 to 2.0 for Gemini; default is 1.0
            "top_p": 0.95,
            "top_k": 20,
        },
    )

    print(response.text)
