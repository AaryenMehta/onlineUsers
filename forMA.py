import requests
  
temp1 = "https://hello.iitk.ac.in/api/"
temp2 = "/onlineUsers"
query = input()

with open('mrym.txt') as f:
    courses = [line.rstrip() for line in f]

flag = False
for course in courses:
    URL = temp1 + course + temp2
    r = requests.get(url = URL)
    data = r.json()
    users = data["studentsOnline"]
    for i in users:
        if i == query:
            print(course[:-2].upper())
            flag = True
if flag == False :
    print("Not Online")