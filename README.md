# 🎬 CineSage

CineSage is an AI-powered Movie Information Extraction System built using LangChain, Mistral AI, and Streamlit.

The application takes a movie description as input and automatically extracts important details such as the movie title, genre, director, cast, release year, themes, and more. It also generates a concise summary of the movie.

---

## 🚀 Features

* Extract Movie Name
* Extract Release Year
* Extract Genre
* Extract Director
* Extract Main Cast
* Extract Main Characters
* Extract Themes
* Extract Key Highlights
* Extract Interesting Facts
* Generate Quick Movie Summary
* Interactive Streamlit UI

---

## 🛠️ Tech Stack

* Python
* LangChain
* Mistral AI
* Prompt Templates
* Streamlit
* dotenv

---

## 📸 Screenshots

### Home Screen

(Add screenshot here)

### Movie Analysis Result

(Add screenshot here)

---

## 📂 Project Structure

```text
CineSage/
│
├── core.py
├── UIcore.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Sarthak-Rajvaidya/CineSage.git
cd CineSage
```

Create a virtual environment:

```bash
uv venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add your API key:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
python -m streamlit run UIcore.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 💡 How It Works

1. User enters a movie description.
2. LangChain Prompt Template structures the request.
3. Mistral AI analyzes the text.
4. Important movie information is extracted.
5. A concise summary is generated.
6. Results are displayed through Streamlit.

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Prompt Engineering
* LangChain Prompt Templates
* Large Language Models (LLMs)
* Information Extraction
* Text Summarization
* Streamlit Deployment
* Building End-to-End GenAI Applications

---

## 🔮 Future Improvements

* Structured Output using Pydantic
* Movie Recommendation System
* Multi-Movie Comparison
* Database Integration
* RAG-based Movie Knowledge Assistant

---

## 👨‍💻 Author

Sarthak Rajvaidya

If you found this project interesting, feel free to star the repository and connect with me on LinkedIn.
