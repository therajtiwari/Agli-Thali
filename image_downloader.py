from bing_image_downloader import downloader
import pandas as pd
import os

# reading the dataset
data = pd.read_csv("cleaned_data.csv")
names = data.name[1:]

for n in names:

    path = "./image_dataset/" + n + "\indian dish" + "/Image_1.jpg"
    # print(path)
    if os.path.exists(path):
        continue

    print("name is", n)
    query_string = n + " indian dish"
    # downloading using bing downloader
    downloader.download(query_string,
                        limit=5,
                        output_dir='static/image_dataset',
                        adult_filter_off=True,
                        force_replace=False,
                        timeout=5)
