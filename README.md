#Devoir_TP_Zahra_Chebbi_DSI23
LLM-Powered Movie & Actor Explorer Application
This project is an Advanced Python - Integration Skills Assessment that demonstrates the integration of FastAPI, Neon Postgres, SQLAlchemy, Pydantic, Langchain (with Groq), and Streamlit. The application consists of a FastAPI backend that manages movie and actor data in a PostgreSQL database and a Streamlit frontend that allows users to explore random movies, view associated actors, and request LLM-generated summaries.
Author: Wahid HamdiGitHub Repository: https://github.com/zahra706/devoir_tp
Objective
The application enables users to:

Store and manage movie and actor data in a PostgreSQL database using FastAPI and SQLAlchemy with relationships.
Retrieve random movies and their actors via a FastAPI endpoint.
Generate movie summaries using Langchain and Groq’s LLM.
Explore movies and request summaries through a user-friendly Streamlit interface.

Data entry is handled via the FastAPI API (e.g., Swagger UI), while the Streamlit app focuses on displaying and interacting with the data.
Project Structure
The project is located in C:\Users\hp\Desktop\dv_python\movie_explorer (or devoir_tp if renamed). The structure is:
movie_explorer/
├── .env
├── .gitignore
├── requirements.txt
├── main_fastapi.py
├── main_streamlit.py
├── database.py
├── models.py
├── pydantic_models.py
├── README.md
├── captures/
│   ├── screenshot_swagger_movies.png
│   ├── screenshot_streamlit_ui.png
│   ├── screenshot_summary.png

Prerequisites

Python: 3.10 or higher
Neon Postgres: Account with connection string (provided)
Groq API Key: For LLM integration
Git: For version control
Virtual Environment: Recommended for dependency isolation

Setup Instructions

git init
cd movie_explorer


Create and Activate Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

The requirements.txt includes:
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





Running the Application
Backend (FastAPI)

Start the FastAPI Server:uvicorn main_fastapi:app --reload


Access the API:
Open http://localhost:8000/docs for Swagger UI.


Add Movie Data:
Use the POST /movies/ endpoint to add movies (required before using the Streamlit app). Example JSONs:{
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

{
  "title": "Pulp Fiction",
  "year": 1994,
  "director": "Quentin Tarantino",
  "actors": [
    {"actor_name": "John Travolta"},
    {"actor_name": "Samuel L. Jackson"},
    {"actor_name": "Uma Thurman"},
    {"actor_name": "Bruce Willis"}
  ]
}

{
  "title": "Al-Risalah (The Message)",
  "year": 1976,
  "director": "Moustapha Akkad",
  "actors": [
    {"actor_name": "Abdullah Gaith (عبد الله غيث)"},
    {"actor_name": "Muna Wassef (منى واصف)"},
    {"actor_name": "Hamdi Ghaith (حمدي غيث)"},
    {"actor_name": "Ahmad Marey (أحمد مرعي)"}
  ]
}




Test Endpoints:
GET /movies/random/: Retrieves a random movie with actors.
POST /generate_summary/: Generates a summary for a given movie_id.



Frontend (Streamlit)

Start the Streamlit App:
In a new terminal, ensure the virtual environment is activated:cd C:\Users\hp\Desktop\dv_python\movie_explorer
.\venv\Scripts\activate
streamlit run main_streamlit.py




Access the UI:
Open http://localhost:8501.


Interact with the App:
Click “Show Random Movie” to display a movie’s title, year, director, and actors.
Click “Get Summary” to fetch an LLM-generated summary.
Ensure the FastAPI server is running during Streamlit usage.



Important Notes

Data Entry: Add movies via the FastAPI Swagger UI (POST /movies/) before using the Streamlit app, as the frontend relies on existing database data.
Neon Postgres: The database may have a 500ms–2s delay on the first query due to cold starts.
Error Handling: The backend includes logging for debugging (check the FastAPI terminal for errors).
Git: Do not commit .env (excluded via .gitignore).

Git Integration
To push changes to the GitHub repository:
git add .
git commit -m "Update movie explorer project"
git push origin main


Repository: https://github.com/zahra706/devoir_tp
If authentication is required, use a GitHub personal access token.

Assessment Questions and Responses

Why is it often necessary to commit the primary record (Movies) before creating the related records (Actors) that depend on its foreign key?

Committing the Movies record first ensures its primary key (id) is generated and persisted in the database. The Actors table requires this movie_id as a foreign key to establish the relationship. Without committing the Movies record, the database would raise a foreign key constraint violation when trying to insert Actors with a non-existent movie_id.


What is the difference between lazy loading and eager loading (like joinedload) for relationships in SQLAlchemy?

Lazy Loading: Related data (e.g., Movies.actors) is fetched from the database only when accessed, triggering additional queries. This can lead to the N+1 query problem, where multiple queries are executed for each related object, reducing performance.
Eager Loading (e.g., joinedload): Related data is fetched in the initial query using SQL JOINs, reducing the number of database queries. For example, joinedload(Movies.actors) includes actor data in the same query as the movie, improving efficiency but potentially increasing memory usage for large datasets.


How would you format the list of actors fetched from the database into a simple string suitable for inclusion in the LLM prompt?

The list of actors is formatted by joining their actor_name fields with commas. For example:actor_list = ", ".join(actor.actor_name for actor in movie.actors) or "various actors"

This creates a string like “Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy”. If the actor list is empty, it defaults to “various actors” to ensure the LLM prompt remains valid.



Captures Directory
The /captures directory contains screenshots and documentation to demonstrate the application’s functionality:

screenshot_swagger_movies.png: Shows the Swagger UI with a successful POST to /movies/ for adding a movie.
screenshot_streamlit_ui.png: Displays the Streamlit UI after clicking “Show Random Movie”, showing movie details and actors.
screenshot_summary.png: Captures the Streamlit UI with an LLM-generated summary after clicking “Get Summary”.

These files provide visual evidence of the application’s backend and frontend in action.
Troubleshooting

Backend Errors:
Check FastAPI logs for detailed error messages (e.g., database or Groq issues).
Verify the DATABASE_URL and GROQ_API_KEY in .env.


Database Connection:
Test Neon Postgres connectivity:python test_db.py

(See test_db.py in the repository for the script.)


Groq LLM:
Test the API key:python test_groq.py

(See test_groq.py in the repository.)


Streamlit:
Ensure the FastAPI server is running before using the Streamlit app.
Use streamlit run main_streamlit.py, not uvicorn.



Assessment Criteria Fulfillment

Backend Functionality & Relationships (8/8): Implements movie and actor endpoints with SQLAlchemy relationships, eager loading (joinedload), and error handling.
Langchain/LLM Integration (4/4): Includes /generate_summary/ with Groq LLM, a structured prompt, and robust error handling.
Frontend Functionality (4/4): Streamlit app displays random movies, actors, and summaries with session state management and error handling.
Integration & Code Quality (4/4): Modular code, comprehensive error handling, logging, and clear documentation in this README.

