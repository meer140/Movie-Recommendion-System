import streamlit as st
import pickle 
import pandas as pd
import requests

st.title("Movie Recommender System")

movies = pickle.load((open("movies.pkl","rb")))
movies = pd.DataFrame(movies)
selected_movie_name = st.selectbox(
    "Select a movie.",
    (movies.title)
)

#fetch image path
def fetch_image(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key=40616226cbae5561ec8188705995d589"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data["poster_path"]


similarity = pickle.load((open("similarity.pkl","rb")))
def recommend(movie):
    movie_idx = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_idx])),reverse=True,key = lambda x : x[1])
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_image(movie_id))
        
    return recommended_movies,recommended_movies_posters


    
if st.button("Recommend"):
    name,posters = recommend(selected_movie_name)
    cols = st.columns(5)
    
    for i,col in enumerate(cols):
        with col:
            st.image(posters[i])
            st.text(name[i])
            