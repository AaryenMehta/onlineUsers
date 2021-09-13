import requests
import time
  
temp1 = "https://hello.iitk.ac.in/api/"
temp2 = "/onlineUsers"
query = input()

time1 = time.time()

with open('data.txt') as f:
    courses = [line.rstrip() for line in f]

flag = False
for course in courses:
    URL = temp1 + course + temp2
    r = requests.get(url = URL)
    data = r.json()
    users = data["studentsOnline"]
    for i in users:
        if i == query:
            print(course)
            flag = True

if flag == False :
    print("Not Online")
time2 = time.time()
print(f'Took {time2-time1:.2f} s')