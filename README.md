🎬 LLM-Powered Movie & Actor Explorer
Projet d’Intégration – Zahra Chebbi, DSI23
Explore random movies, discover their casts, and generate intelligent summaries using FastAPI, PostgreSQL (Neon), SQLAlchemy, Langchain, Groq, and Streamlit.
🧠 This project combines structured data management with LLM intelligence for an enriched cinematic experience.
📁 GitHub Repository: zahra706/devoir_tp👨‍🏫 Supervisor: Wahid Hamdi👩‍🎓 Student: Zahra Chebbi – DSI23  
🚀 Features

✅ Store movies and actors with relational integrity.
✅ Retrieve and display random movies with their casts.
✅ Generate intelligent movie summaries via Langchain and Groq.
✅ Simple and intuitive Streamlit user interface.
✅ Swagger UI for testing the FastAPI backend.

🧱 Project Architecture
movie_explorer/
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── main_fastapi.py        # FastAPI backend
├── main_streamlit.py      # Streamlit frontend
├── database.py            # Database connection
├── models.py              # SQLAlchemy models
├── pydantic_models.py     # Pydantic schemas
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── captures/              # Screenshots
│   ├── 1.png              # Swagger UI
│   ├── 2.png              # Streamlit UI
│   ├── 3.png              # Generated summary

⚙️ Prerequisites

Python: ≥ 3.10
Git: For version control
Neon PostgreSQL: Account with connection string
Groq API Key: For LLM integration
Virtual Environment: Recommended for dependency isolation

🛠️ Installation & Setup

Clone the Repository:
git clone https://github.com/zahra706/devoir_tp.git
cd movie_explorer


Create and Activate Virtual Environment:
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install Dependencies:
pip install -r requirements.txt

requirements.txt:
fastapi==0.115.2
uvicorn==0.32.0
sqlalchemy==2.0.36
psycopg2-binary==2.9.10
pydantic==2.9.2
streamlit==1.39.0
langchain==0.3.3
langchain-groq==0.2.0
requests==2.32.3
python-dotenv==1.0.1


Configure Environment Variables:

Create a .env file in the project root:DATABASE_URL=postgresql://moviedb_owner:npg_FJjnSrI6gb7D@ep-soft-tree-a42rjmby-pooler.us-east-1.aws.neon.tech/moviedb?sslmode=require
GROQ_API_KEY=xai-AA95YZvfir0uS1vGlJJEqjzq6iZYlY5gVbENSJEuu68ssExmY8j1KSex3FmBixA3Sx6TDQnfqw9sEMen





▶️ Running the Application
1️⃣ Backend (FastAPI)

Start the FastAPI Server:
uvicorn main_fastapi:app --reload


Access Swagger UI:

Open http://localhost:8000/docs.


Add Movie Data:

Use POST /movies/ in Swagger UI to add movies (required before using Streamlit). Example:{
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


Add additional movies like “Pulp Fiction” and “Al-Risalah (The Message)” as per the assessment.



2️⃣ Frontend (Streamlit)

Start the Streamlit App:
# Ensure virtual environment is activated
.\venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/macOS
streamlit run main_streamlit.py


Access the Interface:

Open http://localhost:8501.


Interact:

Click “Show Random Movie” to view a movie’s details and cast.
Click “Get Summary” to generate an LLM-powered summary.
Ensure the FastAPI server is running.



🧪 API Endpoints



Endpoint
Description



GET /movies/random/
Retrieves a random movie with its actors


POST /movies/
Adds a movie with associated actors


POST /generate_summary/
Generates an intelligent summary via Groq


📷 Screenshots
The /captures directory contains:

1.png: Swagger UI showing POST /movies/ in action.
2.png: Streamlit interface displaying a random movie and cast.
3.png: Streamlit interface with a generated summary.

❓ Assessment Questions & Answers

Why insert the movie before the actors?

The Movies record must be committed first to generate its primary key (id), which is used as a foreign key (movie_id) in the Actors table. Committing the movie ensures the foreign key constraint is satisfied, preventing database errors.


Difference between Lazy Loading and Eager Loading (joinedload)?

Lazy Loading: Related data (e.g., actors) is loaded only when accessed, triggering additional queries. This can lead to N+1 query issues, reducing performance.
Eager Loading (joinedload): Related data is fetched in a single query using SQL JOINs, improving efficiency. In this project, joinedload(Movies.actors) ensures actors are loaded with movies in one query.


How to format actors for the LLM prompt?
actor_list = ", ".join(actor.actor_name for actor in movie.actors) or "various actors"


This joins actor names with commas (e.g., “Leonardo DiCaprio, Joseph Gordon-Levitt”). If no actors are present, it defaults to “various actors” for a valid prompt.



🌐 Git Versioning
git add .
git commit -m "Update movie explorer project"
git push origin main


Repository: https://github.com/zahra706/devoir_tp
Use a GitHub personal access token if authentication is required.

🎓 About
This project is part of Zahra Chebbi’s integration assignment for DSI23. It showcases synergy between a robust backend, an LLM-powered summary generator, and a user-friendly frontend, adhering to Python development best practices.




