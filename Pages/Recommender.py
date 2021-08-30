import pandas as pd
import numpy as np
import streamlit as st
import os
from bokeh.models.widgets import Div
from PIL import Image

def eda():
    Bangalore = pd.read_csv('Data/Banglore/Banglore1.csv', sep=',')
    Delhi = pd.read_csv('Data/Delhi/Delhi1.csv', sep=',')
    Pune = pd.read_csv('Data/Pune/Pune1.csv')
    Kolkata = pd.read_csv('Data/Kolkata/Kolkata1.csv')
    Mumbai = pd.read_csv('Data/Mumbai/Mumbai1.csv')

    option = st.selectbox('Select Your State', ('Bangalore','Delhi','Pune', 'Kolkata', 'Mumbai'))

    #Details of every resturant

    def recom(dataframe):
        dataframe = dataframe.drop(["Unnamed: 0","updated_url"],axis=1)
        data_new =dataframe

        data_new['Cuisine'].value_counts().sort_values(ascending=False).head(10)

        C = data_new['Rating'].mean()
        m = data_new['Rating Count'].mean()
        data_new_copy = data_new 
        q_restaurant = data_new_copy.loc[data_new['Rating Count'] >= m]
        

        # Function that computes the weighted rating of each restaurant
        def weighted_rating(x, m=m, C=C):
            v = x['Rating']
            R = x['Rating Count']
            # Calculating the score
            return (v/(v+m) * R) + (m/(m+v) * C)
        # Define a new feature 'score' and calculate its value with `weighted_rating()`
        q_restaurant['score'] = q_restaurant.apply(weighted_rating, axis=1)
        #Sort restaurant based on score calculated above
        q_restaurant = q_restaurant.sort_values('score', ascending=False)
        #Print the top 10 restaurants in New Jersey
        dataframe = q_restaurant.drop_duplicates().head(10)

        title = st.selectbox('Select Your Restaurant', (list(dataframe['Name'])))

        if title in dataframe['Name'].values:
            Rating = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Rating'])
            st.markdown("### Restaurant Rating:-")
            #RATINGS
            if Rating == 4.5:
                image = Image.open('Data/Ratings/4.5.png')
                st.image(image, use_column_width=True)


            elif Rating == 4.0:
                image = Image.open('Data/Ratings/4.png')
                st.image(image, use_column_width=True)


            elif Rating == 3.5:
                image = Image.open('Data/Ratings/3.5.png')
                st.image(image, use_column_width=True)

            else:
                pass

            #CUISINE OF RESTURANT
            Cuisine = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Cuisine'])
            st.markdown("### Restaurant Cuisine:-")
            st.error(Cuisine)

            #LOCATION
            Address = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Address'])
            st.markdown("### The Address:-")
            st.success(Address)

            #CONTACT DETAILS
            Telephone = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Telephone'])
            if Telephone == "Not Available":
                pass

            else:
                st.markdown("### Contact Details:-")
                st.info('Phone:- '+ Telephone)

            #URL
            url = (Bangalore.at[Bangalore['Name'].eq(title).idxmax(), 'updated_url'])
            st.markdown("### The Website:-")
            if st.button("Zomato Website"):
                    #js = "window.open" + "('" + url + "')"  # New tab
                    js = "window.location.href" + " = " + "'" + url + "'"  # Current tab
                    html = '<img src onerror="{}">'.format(js)
                    div = Div(text=html)
                    st.bokeh_chart(div)
        
        st.text("")
        image = Image.open('Data/happyeating.png')
        st.image(image, use_column_width=True)

    if option == 'Bangalore':
        image = Image.open('Data/top_10.jpg')
        st.image(image, use_column_width=True)
        recom(Bangalore)



    elif option == 'Delhi':
        image = Image.open('Data/top_10.jpg')
        st.image(image, use_column_width=True)
        recom(Delhi)

    elif option == 'Pune':
        image = Image.open('Data/top_10.jpg')
        st.image(image, use_column_width=True)
        recom(Pune)

    elif option == 'Mumbai':
        image = Image.open('Data/top_10.jpg')
        st.image(image, use_column_width=True)
        recom(Mumbai)

    elif option == 'Kolkata':
        image = Image.open('Data/top_10.jpg')
        st.image(image, use_column_width=True)
        recom(Kolkata)

