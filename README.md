🎬 LLM-Powered Movie & Actor Explorer
Advanced Python Integration Project – Zahra Chebbi, DSI23

Explore random movies, discover their actors, and generate intelligent summaries using FastAPI, Neon PostgreSQL, SQLAlchemy, Langchain, Groq, and Streamlit.

🧠 This app combines the power of structured data with the capabilities of modern LLMs for an enriched movie exploration experience.

📁 GitHub Repository: zahra706/devoir_tp
👩‍💻 Author: Wahid Hamdi
📅 Student: Zahra Chebbi – DSI23

🚀 Features
✅ Store and manage Movies and Actors with relational integrity.
✅ Explore random movies and view their cast.
✅ Generate LLM-based summaries using Langchain + Groq.
✅ Browse content via an elegant Streamlit frontend.
✅ Use FastAPI Swagger UI for data entry.

🧱 Project Architecture
bash
Copier
Modifier
movie_explorer/
├── .env
├── .gitignore
├── main_fastapi.py        # FastAPI backend
├── main_streamlit.py      # Streamlit frontend
├── database.py
├── models.py
├── pydantic_models.py
├── requirements.txt
├── README.md
├── captures/
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
⚙️ Requirements
Python ≥ 3.10

Git

Neon Postgres account

Groq API Key

Virtual Environment (recommended)

🛠️ Installation & Setup
bash
Copier
Modifier
# 1. Clone repository
git clone https://github.com/zahra706/devoir_tp.git
cd devoir_tp

# 2. Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
📦 requirements.txt includes:
php
Copier
Modifier
fastapi, uvicorn, sqlalchemy, psycopg2-binary, pydantic,
streamlit, langchain, langchain-groq, requests, python-dotenv
🔐 Environment Variables
Create a .env file in the root:

env
Copier
Modifier
DATABASE_URL=postgresql://<your_connection_string>
GROQ_API_KEY=<your_groq_api_key>
▶️ Running the App
1️⃣ Start the FastAPI Backend
bash
Copier
Modifier
uvicorn main_fastapi:app --reload
📌 Access Swagger UI: http://localhost:8000/docs

2️⃣ Add Sample Movies (Swagger UI)
Use POST /movies/ with:

json
Copier
Modifier
{
  "title": "Inception",
  "year": 2010,
  "director": "Christopher Nolan",
  "actors": [
    {"actor_name": "Leonardo DiCaprio"},
    {"actor_name": "Joseph Gordon-Levitt"},
    {"actor_name": "Elliot Page"},
    {"actor_name": "Tom Hardy"}
  ]
}
Add more examples from the original README if needed.

3️⃣ Start the Streamlit Frontend
In a new terminal:

bash
Copier
Modifier
# Activate venv again if needed
cd devoir_tp
.\venv\Scripts\activate  # Windows
streamlit run main_streamlit.py
📌 Access UI: http://localhost:8501

🧪 API Endpoints
Endpoint	Description
GET /movies/random/	Retrieve a random movie and its actors
POST /generate_summary/	Generate LLM summary for a movie by movie_id

📷 Screenshots (captures/)
Swagger UI	Streamlit App	Summary

❓ Assessment Q&A
🔸 Why insert the Movie before Actors?
Because the movie_id foreign key in Actor must reference an existing movie. Committing the movie ensures its id is available for the related actors.

🔸 Lazy Loading vs. Eager Loading (joinedload)
Lazy: Fetch related data only when accessed. May cause many small queries (N+1 problem).

Eager (joinedload): Fetch related data in one SQL JOIN query. Efficient for known use cases.

🔸 Format actors for LLM prompt
python
Copier
Modifier
actor_list = ", ".join(actor.actor_name for actor in movie.actors) or "various actors"
🧩 Troubleshooting
Issue	Solution
Backend errors	Check FastAPI terminal logs
Groq API not working	Test with python test_groq.py
Database not connecting	Use python test_db.py
Streamlit not loading	Ensure FastAPI is running first

🌐 Git Versioning
bash
Copier
Modifier
git add .
git commit -m "Update movie explorer project"
git push origin main


🎓 This project is part of Zahra Chebbi’s integration assessment for DSI23 – showcasing backend/frontend synergy, AI usage, and clean development practices.
