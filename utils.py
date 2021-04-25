import pandas as pd
import pickle

# global vars
data = None
model = None
model_data_frame = None


# loading the datasets and trained model
def loadArtifacts():
    global data, model, model_data_frame
    data = pd.read_csv("./artifacts/cleaned_data.csv")
    model_data_frame = pd.read_csv("./artifacts/model_data.csv",
                                   index_col="name")
    with open("./artifacts/model.pickle", "rb") as f:
        model = pickle.load(f)


# getting the names of all dishes
def getDishNames():
    dishes_names = data.name.to_list()
    diet_of_dishes = data.diet.to_list()
    return dishes_names, diet_of_dishes


# getting the dishes based on diet(veg or non-veg)
def getDietWiseDishes(diet):
    global data
    if diet == "vegetarian":
        df = data.loc[data.diet == diet, ["name", "diet"]]
        return df.name, df.diet
    elif diet == "non-vegetarian":
        df = data.loc[data.diet == diet, ["name", "diet"]]
        return df.name, df.diet
    else:
        return getDishNames()  #no filtering (both type of diet)


# getting the dishes based on states
def getStateWiseDishes(state, diet):
    global data
    verify_state = state in data.state.to_list()
    diet = diet.lower()
    if diet == "vegetarian" or diet == "non-vegetarian":
        if verify_state:
            if state == "All State":
                return getDietWiseDishes(diet)
            else:
                df = data.loc[(data.state == state) & (data.diet == diet),
                              ["name", "diet"]]
                return df.name, df.diet
        else:
            return getDietWiseDishes(diet)  #returning all states
    else:
        if verify_state:
            if state == "All State":
                return getDishNames()
            else:
                df = data.loc[data.state == state, ["name", "diet"]]
                return df.name, df.diet
        else:
            return getDishNames()


# getting dishes based on the region
def getRegionWiseDishes(region, diet):
    global data
    verify_region = region.title() in data.region.to_list()
    diet = diet.lower()
    if diet == "vegetarian" or diet == "non-vegetarian":
        if verify_region:
            if region == "All Region":
                return getDietWiseDishes(diet)
            else:
                df = data.loc[(data.region == region.title()) &
                              (data.diet == diet), ['name', 'diet']]
                return df.name, df.diet
        else:
            return getDietWiseDishes(diet)  #returning all regions
    else:
        if verify_region:
            if region == "All Region":
                return getDietWiseDishes(diet)
            else:
                df = data.loc[(data.region == region.title()),
                              ['name', 'diet']]
                return df.name, df.diet
        else:
            return getDietWiseDishes(diet)  #returning all regions


# getting the name of all the states
def getStateNames():
    global data
    return list(data.state.unique())


# getting the youtube source video link of the dish
def getRecipe(dish):
    global data
    return data.loc[data.name == dish, ["recipe"]].values[0][0]


# getting the top 12 recommendations with the help of the trained model
def getRecommendation(dish):
    global model, model_data_frame
    X = model_data_frame[model_data_frame.index == dish]
    distance, dishes_index = model.kneighbors(X, n_neighbors=13)
    recommendations = []
    for dish_index in dishes_index.flatten():
        recommended_dish = model_data_frame.index[dish_index]
        if recommended_dish == dish:  #self-dish
            continue
        else:
            recommendations.append(recommended_dish)
    return recommendations
