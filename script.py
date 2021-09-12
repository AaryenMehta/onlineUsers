import json

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

if __name__ == "__main__":
    sourceFile = open('demo.txt','a')
    fname = "convertjson"
    for _ in range(1,12,1):
        my_data = js_r(fname+str(_)+".json")
        print(fname+str(_)+".json")
        for i in my_data:
            if type(i) == type("abds") :
                print(i)
            temp = i["Course"][152:]
            id = 0
            while temp[id] != ':' :
                id += 1
            print(i["Course"][152:152+id].lower()+"21",file=sourceFile)
    sourceFile.close()