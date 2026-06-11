import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

# -----------------------
# Load Environment
# -----------------------
load_dotenv()

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Movie Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.markdown(
    "Paste a movie description and extract structured information using LangChain + Pydantic."
)

# -----------------------
# LLM
# -----------------------
model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.9,
    max_tokens=500
)

# -----------------------
# Pydantic Schema
# -----------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genere: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# -----------------------
# Parser
# -----------------------
parser = PydanticOutputParser(
    pydantic_object=Movie
)

# -----------------------
# Prompt
# -----------------------
template = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instruction}
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])

# -----------------------
# Input Area
# -----------------------
paragraph = st.text_area(
    "Movie Description",
    height=250,
    placeholder="Paste movie description here..."
)

# -----------------------
# Button
# -----------------------
if st.button("Extract Information"):

    if not paragraph.strip():
        st.warning("Please enter a movie description.")
    else:

        try:

            with st.spinner("Analyzing Movie..."):

                prompt = template.invoke({
                    "paragraph": paragraph,
                    "format_instruction":
                        parser.get_format_instructions()
                })

                response = model.invoke(prompt)

                movie = parser.parse(
                    response.content
                )

            st.success("Extraction Completed")

            st.subheader("🎥 Movie Details")

            st.write(
                f"**Title:** {movie.title}"
            )

            st.write(
                f"**Release Year:** {movie.release_year}"
            )

            st.write(
                f"**Director:** {movie.director}"
            )

            st.write(
                f"**Rating:** {movie.rating}"
            )

            st.write(
                f"**Genres:** {', '.join(movie.genere)}"
            )

            st.write(
                f"**Cast:** {', '.join(movie.cast)}"
            )

            st.subheader("📝 Summary")

            st.info(movie.summary)

        except Exception as e:

            st.error(
                "Failed to parse structured output."
            )

            st.exception(e)