import streamlit as st
from Pages import Home, bts_eda, Recommender


#st. sidebar.image('Data/Recommender.png',use_column_width=500)
st.sidebar.title("All about the App...")

option = st.sidebar.radio(
    'Navigate through various features of the app!',
    ('Home.', 'Our List of Restaurants.','Restuarants We Recommend.')
)

if option == 'Home.':
    Home.home()

if option == 'Our List of Restaurants.':
    bts_eda.eda()

if option == 'Restuarants We Recommend.':
    Recommender.eda()


st.sidebar.text("")
st.sidebar.title("")
st. sidebar.image('Data/zomato.png',use_column_width=500)
