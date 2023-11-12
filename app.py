import streamlit as st
import pickle
import pandas as pd 

# Loading movies
movies_list = pd.read_pickle('movies.pkl') 
similarity = pickle.load(open("similarity.pkl", "rb"))


def recommend(selected_movie_name):
    
    movie_index = movies_list[movies_list['title'] == selected_movie_name].index[0]
    distances = similarity[movie_index]
    
    movies_list['similarity'] = distances  # Add a 'similarity' column to the DataFrame
    recommended_movies = movies_list.sort_values(by='similarity', ascending=False)[1:6]
    
    # Extract the recommended movie titles from the DataFrame
    recommended_movie_titles = recommended_movies['title'].values
    
    return recommended_movie_titles

# Streamlit app
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie of your choice",
    movies_list["title"].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.write("Recommended Movies:")
    for movie_title in recommendations:
        st.write(movie_title)


