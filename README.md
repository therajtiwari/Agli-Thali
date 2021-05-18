# AgliThali- An Indian Food Recommender

## General info

This project recommends Indian Dishes based on the input of the user using Cosine similarity algorithm.
User can filter the results based on the diet type, states as well as the regions.

## Technologies

Project is created with:

- Python
- Numpy
- Pandas
- Seaborn
- Flask
- HTML,CSS
- Bootstrap

## Dataset used

[Indian Food 101](https://www.kaggle.com/nehaprabhavalkar/indian-food-101)

## Project Structure

This project has four major parts :

1. model.ipynb - This contains code fot our Machine Learning model to recommend the dishes using tha data in 'cleaned_data.csv' file.
2. application.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the recommended dish based on our model and returns it.
3. utils.py - This contains the all the functions used in application.py to handle the requests that are made.
4. templates - This folder contains the HTML template to allow user to select the dishes and filters and displays the recommended dishes.

## Setting up a development environment and running the app

I assume that you have `git` and `virtualenv` installed.

    #Clone the code repository into ~/dev/my_app
    mkdir -p ~/dev
    cd ~/dev
    git clone https://github.com/therajtiwari/Indian_food_recommendation_system.git my_app

    #Create the 'my_app' virtual environment
    mkvirtualenv -p PATH/TO/PYTHON my_app

    #Install required Python packages
    cd ~/dev/my_app
    workon my_app
    pip install -r requirements.txt

    #Run the app
    PATH/TO/PYTHON application.py

## Project Screenshots:

<p align="center">
  <img src="./assets/react-integration-3.gif" width="80%" alt="react easybase integration 1">
  <br />
  <br />
  <img src="./assets/users-2.gif" width="80%" alt="react easybase integration 2">
</p>
