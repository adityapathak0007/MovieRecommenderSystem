import streamlit as st
import pickle
import pandas as pd
import gdown
import requests

def download_file(url, filename):
    try:
        gdown.download(url, filename, quiet=False)
        st.success(f"File downloaded successfully: {filename}")
    except Exception as e:
        st.error(f"Failed to download file: {e}")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    else:
        return "https://via.placeholder.com/500x750?text=Poster+Not+Available"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Download and load similarity matrix
file_url = "https://drive.google.com/uc?id=1nRxFIkLs-lfRtUVozJCUAEssNkiigzd8"
download_file(file_url, 'similarity.pkl')

try:
    with open('similarity.pkl', 'rb') as file:
        similarity = pickle.load(file)
        st.success("Pickle file loaded successfully.")
except Exception as e:
    st.error(f"Error loading pickle file: {e}")

# Load movie dictionary
try:
    with open('movie_dict.pkl', 'rb') as file:
        movies_dict = pickle.load(file)
        movies = pd.DataFrame(movies_dict)
        st.success("Movie dictionary loaded and DataFrame created successfully.")
except Exception as e:
    st.error(f"Error loading movies pickle file: {e}")

st.title('Movie Recommender System')

# Ensure `movies` DataFrame is not empty
if not movies.empty:
    selected_movie_name = st.selectbox(
        'Select a movie',
        movies['title'].values
    )

    if st.button('Show Recommendation'):
        if 'similarity' in locals():
            recommended_movies, recommended_movies_posters = recommend(selected_movie_name)
            cols = st.columns(5)
            for col, movie, poster in zip(cols, recommended_movies, recommended_movies_posters):
                with col:
                    st.text(movie)
                    st.image(poster)
        else:
            st.error("Similarity matrix is not loaded. Please check the file.")
else:
    st.error("Movies data is not loaded. Please check the file.")
