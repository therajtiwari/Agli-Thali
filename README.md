# Indian Food Recommender

## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)

## General info

This project is simple Lorem ipsum dolor generator.

## Technologies

Project is created with:

- Lorem version: 12.3
- Ipsum version: 2.33
- Ament library version: 999

## Setup

To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```

## Project Structure

This project has four major parts :

1. model.ipynb - This contains code fot our Machine Learning model to recommend the dishes using tha data in 'cleaned_data.csv' file.
2. application.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the recommended dish based on our model and returns it.
3. utils.py - This contains the all the functions used in application.py to handle the requests that are made.
4. templates - This folder contains the HTML template to allow user to select the dishes and filters and displays the recommended dishes.

## Setting up a development environment

├── migrations
│ ├── README
│ ├── alembic.ini
│ ├── env.py
│ ├── script.py.mako
│ └── versions
│ └── ee69294e63e_init_state.py

We assume that you have `git` and `virtualenv` installed.

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
