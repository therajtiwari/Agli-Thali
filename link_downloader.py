from youtubesearchpython import VideosSearch
import pandas as pd
import json
# here i read csv file of cleaned data
data = pd.read_csv("cleaned_data.csv")


if "recipe" not in data.columns:
    data["recipe"] = "empty"  # here i created a recipe column with empty string


def getVideoID(dish):

    videosSearch = VideosSearch(str(dish), limit=1)
    info = videosSearch.result()
    return (((info["result"])[0]["id"]))


for i in range(data.shape[0]):

    # if there is unique id available then it's not going to run again
    # if data.loc[i, "recipe"] == "empty":
    #     # here i get a name of dish base on index from loop
    dish = data.loc[i, "name"]
    id = getVideoID(dish)
    print(id)
    print(i, "----------------")
    #     # below i store a recipe video unique id to appropriate index
    data.loc[i, "recipe"] = id
    data.to_csv("cleaned_data.csv", index=False)
#     # here again save a csv file which contain all data and recipe's unique youtube id
#     data.to_csv("artifacts/cleaned_data.csv", index=False)
