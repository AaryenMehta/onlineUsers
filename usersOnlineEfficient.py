import asyncio
import aiohttp
import time
import ast
import json

flag = False

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)


def prettyPrint(url):
    temp = url[29:]
    for id in range(len(temp)):
        if temp[id] == "/":
            break
    print(url[29:id+27].upper())


async def get(url, session):
    global flag
    try:
        async with session.get(url=url) as response:
            resp = await response.read()
            dictstr = resp.decode("UTF-8")
            data = ast.literal_eval(dictstr)
            for i in data["studentsOnline"] :
                if i == query:
                    flag = True
                    prettyPrint(url)
    except Exception as e:
        pass


async def main(urls):
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[get(url, session) for url in urls])


if __name__ == "__main__":

    websites = str()
    query = input()

    try :
        query = int(query)
    except :
        pass

    if type(query) == type(1) :
        query = str(query)
        f = js_r("students.json")
        try:
            query = f[query]
        except:
            print("No such roll number exists!!")

    with open("websites.txt") as f:
        for line in f:
            websites += line

    urls = websites.split("\n")
    start = time.time()
    asyncio.run(main(urls))
    end = time.time()
    if flag == False:
        print("Not Online!!")
    print("Took {} seconds to pull {} websites.".format(end - start, len(urls)))