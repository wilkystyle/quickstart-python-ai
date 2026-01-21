# quickstart-python-ai
A minimal example of using the Gemini free tier in Python.

## Prerequisites
1. Get a [Google AI Studio API key](https://aistudio.google.com/app/api-keys)
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/).
3. Create a `.env` file in this directory with the following contents:

```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

## Usage

```bash
uv venv -cp 3.12
uv pip install google-genai python-dotenv
uv run python chat.py
```
