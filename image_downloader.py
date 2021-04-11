from bing_image_downloader import downloader
import pandas as pd
import os

data = pd.read_csv("cleaned_data.csv")
names = data.name[179:]

for n in names:

    path = "./image_dataset/" + n

    if os.path.exists(path):
        continue

    query_string = n + " indian dish"
    downloader.download(query_string,
                        limit=5,
                        output_dir='static/image_dataset',
                        adult_filter_off=True,
                        force_replace=False,
                        timeout=30)
