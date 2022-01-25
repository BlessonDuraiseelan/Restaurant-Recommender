# Restaurant-Recommender

A Recommendation app that is designed to choose popular restaurants as well as available Restaurants for a user based on the user choice.
The cities chosen for showing the output are :Banglore, Mumbai, Pune, Delhi, Kolakta.
The app will output the availabe restaurants with top 10 popular restaurants on the location provided by the user.

# Dataset and Modelling 

The app has been developed by the food Dataset provided by Zomato API.The dataset contained multiple cities. EDA Techniques has been applied on the Data to fetch the required data for the five cities . Once the data for the five selected cities were chosen they were collected into one document and was used as a single dataset.

Once the dataset was obtained various visualisation properties were applied to draw insight and preprocessing methods were applied to check for cleanliness and data correctness.
Then we work upon  the obtained data and apply weighted ratings that will be used for fetching the hotels and used for the purpose of  recommendation.
The app will be recommended on the Ratings and also the provision of website of the hotel is also available for the user.

Streamlit was used to build the app with the help of Python. The app contains of multiple sections where the user can choose the city of their choice. Once the city has been chosen the available restaurnats will be shown to the user. And after the choice has been applied for fetching the popular restaurants the app will show the top 10 restaurnats which has been decided on the basis of weighted rating. Along with the provision of the app to show top restaurnats the zomato link of the restaurnat is also availablw which can be used to access the facilites of the hotel.
The app was deployed on the web with the help of Heroku. There will be feature of top restaurant and the availbale restaurants.

![7](https://user-images.githubusercontent.com/76935226/150986050-4945ce83-e27b-4bc3-8aba-2e34e286ac70.png)

![image](https://user-images.githubusercontent.com/76935226/150985601-7753aef2-4204-4171-a3d7-f61fbb02419a.png)

![image](https://user-images.githubusercontent.com/76935226/140600973-8be7034a-18d3-4a27-aa3e-3fcfdde98eea.png)

# Check out the App
https://restaurantrecommenders.herokuapp.com/

![Screenshot (150)](https://user-images.githubusercontent.com/76935226/140601233-4f89b14a-10ae-43f0-80e4-628d27eaba52.png)
![Screenshot (151)](https://user-images.githubusercontent.com/76935226/140601206-7a9826ca-0569-48dd-83a6-d324827276e5.png)
![Screenshot (152)](https://user-images.githubusercontent.com/76935226/140601211-ba5e0aee-da4c-4775-97f5-1088163b0d8f.png)





