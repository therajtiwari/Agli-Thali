import os
import pandas as pd

d = os.path.dirname(os.path.realpath(__file__))

data = pd.read_csv("cleaned_data.csv")
names = data.name[1:]

l = []
# for n in names:
#     fn = n + " indian dish"
#     if fn not in os.listdir(d):
#         # if path == "check.py":
#         #     continue
#         # full_path = os.path.join(d, path)
#         # count = len([name for name in os.listdir(full_path)])
#         # if (count < 5):
#         #     l.append(path)
#         l.append(n)

for n in os.listdir(d):
    if (n != "check.py" and n != "cleaned_data.csv"):
        for file in os.listdir(os.path.join(d, n)):
            # print(file)
            # base = file.split(".")
            # ext = base[1]
            # name = base[0]
            # if (ext != "jpg"):
            #     print(base)
            base = os.path.splitext(file)
            # print(base)
            ext = base[1]
            name = base[0]

            if (str(ext) != ".jpg"):
                # print(base)
                os.rename()
            # print(temp)
    print("\n")

print(l)