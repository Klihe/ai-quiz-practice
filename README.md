# Lightweight Quiz Application for Studying

## Description
- A quiz application that checks answers to questions automatically using OpenAI API.
- Application can have ciritical bugs and is for demo purposes only.

## Setup
insert api key into `.env` file as `OPENAI_API_KEY=your_api_key`

## Run
`uv run -m streamlit run src/main.py`

## Add your own quiz:
1. Create a new JSON file that follow the structure of `example.json` in the `resources` folder.
```json
{
  "questions": [
    {
      "question": "What is the capital of France?",
      "answer": "Paris"
    },
    {
      "question": "What is 2 + 2?",
      "answer": "4"
    }
  ]
}
```
2. Start application and upload the JSON file using the file uploader in `add_delete` tab.
3. Make sure you choose quiz inside `manage` tab after uploading the file. (If you don't see the quiz try refreshing the page `ctrl+r`)
4. Start quizzing yourself in the `quiz` tab!