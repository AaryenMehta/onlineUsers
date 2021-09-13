import requests
import json

URL = "https://search.pclub.in/api/students"
r = requests.get(url = URL)
data = r.json()
newD = dict()
for i in data:
    newD[i["i"]] = i["u"]
with open("students.json","w") as f:
    json.dump(newD,f)
print(newD)