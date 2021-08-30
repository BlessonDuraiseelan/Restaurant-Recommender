import streamlit as st
from PIL import Image

def home():
    image = Image.open('Data/Food.jpg')
    st.image(image, use_column_width=True)
    st.warning("The app to get you to the closest and most highly rated places to eat!")
    st.markdown("Based on data from Zomato, the app covers restaurants form 5 cities across Bangalore, Delhi, Mumbai, Kolkata and Pune to recommend the 10 most highly rated restaurants in each city. ")
    st.success("Because hunger is also an emergency!! :ambulance:" ":100:")


