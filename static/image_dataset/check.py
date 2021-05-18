import os
import pandas as pd

d = os.path.dirname(os.path.realpath(__file__))

data = pd.read_csv("cleaned_data.csv")
names = data.name[1:]


def getNullImages():
    l = []
    for n in names:
        fn = n + " indian dish"
        if fn not in os.listdir(d):
            # if path == "check.py":
            #     continue
            # full_path = os.path.join(d, path)
            # count = len([name for name in os.listdir(full_path)])
            # if (count < 5):
            #     l.append(path)
            l.append(n)
    print(l)


def renameImages():
    for n in os.listdir(d):
        if (n != "check.py" and n != "cleaned_data.csv"):
            for file in os.listdir(os.path.join(d, n)):
                base = os.path.splitext(file)
                thisfile = os.path.join(d, n, file)
                name = base[0]
                ext = base[1]
                if (ext != ".jpg"):
                    fname = os.path.join(d, n, name + ".jpg")
                    # print(thisfile, fpath)
                    os.rename(thisfile, fname)

    print("\n")


getNullImages()
renameImages()