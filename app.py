import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
st.title('Movie Recommender System')

Selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
     movies['title'].values
)