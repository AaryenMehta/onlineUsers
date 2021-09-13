fn = open("websites.txt","w")
temp1 = "https://hello.iitk.ac.in/api/"
temp2 = "/onlineUsers"
with open("data.txt") as f:
    for line in f:
        print(temp1+line.rstrip()+temp2,file=fn)