import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("🎬 Movie Explorer")

# Initialize session state
if "movie" not in st.session_state:
    st.session_state.movie = None
if "summary" not in st.session_state:
    st.session_state.summary = None

# Button to fetch a random movie
if st.button("Show Random Movie"):
    with st.spinner("Fetching a random movie..."):
        try:
            res = requests.get(f"{API_URL}/movies/random/")
            res.raise_for_status()
            st.session_state.movie = res.json()
            st.session_state.summary = None
        except requests.RequestException as e:
            st.error(f"Failed to fetch movie: {e}. Ensure the FastAPI server is running.")

# Display movie details if available
if st.session_state.movie:
    movie = st.session_state.movie
    st.header(f"{movie['title']} ({movie['year']})")
    st.write(f"**Director:** {movie['director']}")
    st.subheader("Actors:")
    for actor in movie["actors"]:
        st.markdown(f"- {actor['actor_name']}")

    # Button to fetch summary
    if st.button("Get Summary", disabled=not st.session_state.movie):
        with st.spinner("Generating summary..."):
            try:
                movie_id = movie["id"]
                res = requests.post(f"{API_URL}/generate_summary/", json={"movie_id": movie_id})
                res.raise_for_status()
                st.session_state.summary = res.json()["summary_text"]
            except requests.RequestException as e:
                st.error(f"Failed to generate summary: {e}. Ensure the FastAPI server is running.")

    # Display summary if available
    if st.session_state.summary:
        st.subheader("Summary")
        st.info(st.session_state.summary)