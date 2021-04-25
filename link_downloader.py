from youtubesearchpython import VideosSearch
import pandas as pd
import json

# reading the dataset
data = pd.read_csv("cleaned_data.csv")

if "recipe" not in data.columns:
    data["recipe"] = "empty"  #creting a recipe column for each dish


# searching for ID using videosSearch module
def getVideoID(dish):
    videosSearch = VideosSearch(str(dish + "indian dish recipe"), limit=1)
    info = videosSearch.result()
    return (((info["result"])[0]["id"]))


for i in range(data.shape[0]):
    # getting the yotutube id of the video
    dish = data.loc[i, "name"]
    id = getVideoID(dish)
    print(id)
    # filling the column of the dish with the obtained youtube id
    data.loc[i, "recipe"] = id
    data.to_csv("cleaned_data.csv", index=False)
