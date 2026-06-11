import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI

# -------------------------
# Load Environment Variables
# -------------------------
load_dotenv()

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="CineSage",
    page_icon="🎬",
    layout="centered"
)

# -------------------------
# Header
# -------------------------
st.title("🎬 CineSage")

st.markdown(
    "Paste a movie description below and get detailed movie information and a quick summary."
)

# -------------------------
# Prompt Template
# -------------------------
template = PromptTemplate.from_template("""
You are an expert movie analyst.

Analyze the movie description provided below and extract all important information.

Movie Description:
{movie_description}

Tasks:

1. Extract:
   - Movie Name
   - Release Year
   - Genre
   - Director
   - Producers
   - Main Cast
   - Main Characters
   - Runtime (if available)
   - Language (if available)
   - Themes
   - Key Highlights
   - Interesting Facts

2. Generate a concise summary of the movie in 4-6 lines.

3. If any information is not available, write "Not Mentioned".

Provide the response in the following format:

🎬 Movie Information

Movie Name:
Release Year:
Genre:
Director:
Producers:
Main Cast:
Main Characters:
Runtime:
Language:
Themes:
Key Highlights:
Interesting Facts:

📝 Quick Summary
""")

# -------------------------
# Input Box
# -------------------------
movie_description = st.text_area(
    "Movie Description",
    height=250,
    placeholder="Paste movie description here..."
)

# -------------------------
# Analyze Button
# -------------------------
if st.button("Analyze Movie"):

    if not movie_description.strip():
        st.warning("Please enter a movie description.")
    else:

        try:

            with st.spinner("Analyzing..."):

                model = ChatMistralAI(
                    model="mistral-large-latest",
                    temperature=0.9,
                    max_tokens=500
                )

                prompt = template.invoke(
                    {
                        "movie_description": movie_description
                    }
                )

                response = model.invoke(prompt)

            st.success("Analysis Complete")

            st.markdown("## Result")

            st.write(response.content)

        except Exception as e:

            st.error("An error occurred")
            st.exception(e)