from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel

from typing import List,Optional

from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.9,
    max_tokens=500
)

class Movie(BaseModel):

    title: str
    release_year: Optional[int]
    genere: List[str]

    director: Optional[str]

    cast:List[str]

    rating : Optional[float]

    summary : str 
    



parser = PydanticOutputParser(pydantic_object=Movie)









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

paragraph = input("\nEnter movie description:\n\n")

prompt = template.invoke(
    {
        "movie_description": paragraph
    }
)

response = model.invoke(prompt)

print("\n========== RESULT ==========\n")
print(response.content)