import os

d = os.path.dirname(os.path.realpath(__file__))

l = []
for path in os.listdir(d):
    if path == "check.py":
        continue
    full_path = os.path.join(d, path)
    count = len([name for name in os.listdir(full_path)])
    if (count < 5):
        l.append(path)

print(l)