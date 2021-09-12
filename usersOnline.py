import requests
  
temp1 = "https://hello.iitk.ac.in/api/"
temp2 = "/onlineUsers"
query = input()

with open('data.txt') as f:
    courses = [line.rstrip() for line in f]

for course in courses:
    URL = temp1 + course + temp2
    r = requests.get(url = URL)
    data = r.json()
    users = data["studentsOnline"]
    for i in users:
        if i == query:
            print(course)