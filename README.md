# Lightweight Quiz Application for Studying

## Description
- A quiz application that checks answers to questions automatically using OpenAI API. (How to get your own [OPENAI_API_KEY](https://www.analyticsvidhya.com/blog/2024/10/openai-api-key-and-add-credits/))
- Application can have ciritical bugs and is for demo purposes only.

## Setup
insert api key into `.env` file as `OPENAI_API_KEY=your_api_key`

## Run
`uv run -m streamlit run src/main.py`

## Add your own quiz:
1. Create a new JSON file that follow the structure of `example.json` in the `resources` folder.
```json
{
    "title": "Quiz name",
    "quiz": [
        {
            "question": "1. Question?",
            "answer": "Answer to first question."
        },
        {
            "question": "2. Question",
            "answer": "Answer to second question."
        },
        {
            "question": "3. Question",
            "answer": "Answer to third question"
        }
    ]
}
```
2. Start application and upload the JSON file using the file uploader in `add_delete` tab.
3. Make sure you choose quiz inside `manage` tab after uploading the file. (If you don't see the quiz try refreshing the page `ctrl+r`)
4. Start quizzing yourself in the `quiz` tab!
