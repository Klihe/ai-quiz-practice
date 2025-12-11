import json
from pathlib import Path

import streamlit as st

from modules.models.llm import LLM

BASE = Path().parent
RESOURCES_FOLDER = BASE / "resources"

score = 0
llm = LLM()

data = {}

quiz, manage, add_delete = st.tabs(["quiz", "manage", "add_delete"])

with manage:
    st.subheader("Select Course")
    course_files = [f.name for f in RESOURCES_FOLDER.glob("*.json")]
    selected_course = st.selectbox("Choose a course", course_files)

    if selected_course:
        selected_course_path = RESOURCES_FOLDER / selected_course
        with selected_course_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

with quiz:
    st.title(data.get("title", "Untitled Quiz"))
    st.divider()

    quiz = data.get("quiz", [])
    for i, question in enumerate(quiz):
        st.write(f"**{i+1}. {question.get('question', '')}**")
        user_answer = st.text_area("", key=f"{i}_answer")

        if user_answer and st.button("Submit Answer", key=f"{i}_submit"):
                response = llm.ask_quiz(question.get("question", ""), user_answer, question.get("answer", ""))

                marked_correct = st.checkbox("Mark as Correct", value=response.correct, key=f"{i}_correct")
                if marked_correct:
                    st.success("Correct!")
                    score += 1
                else:
                    st.error("Incorrect!")
                    st.warning("Hint: " + str(response.hint))

                st.info("Correct answer: " + question.get("answer", ""))
                st.info(f"Your answer was {response.percentile:.2f}% close to the correct answer.")

        st.divider()

    st.write(f"Your score: {score}/{len(data.get('quiz', []))}")

with add_delete:
    uploaded_files = st.file_uploader("Upload JSON files", type="json", accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            path = Path(RESOURCES_FOLDER) / uploaded_file.name
            with path.open("wb") as file:
                file.write(uploaded_file.getbuffer())

    st.divider()

    resource_files = list(Path(RESOURCES_FOLDER).glob("*.json"))
    if resource_files:
        st.subheader("Remove Files")
        files_to_remove = st.multiselect("Select files to remove", [f.name for f in resource_files])
        if st.button("Delete"):
            for file_name in files_to_remove:
                Path(RESOURCES_FOLDER).joinpath(file_name).unlink()
            st.success(f"Deleted {len(files_to_remove)} file(s)")
