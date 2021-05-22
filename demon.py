import re
import os
import time
import sys

# 时间戳只存在json中
currentPath = os.path.dirname(__file__)
apiPath = os.path.join( currentPath, "api")
timeList = []
for fileName in os.listdir(apiPath):
    filePath = os.path.join(apiPath, fileName)
    with open(filePath, "r", encoding="utf-8") as file:
        fileContent = file.read(-1)
        rex = re.compile("(16[0-9]{8})")
        searchResult = rex.findall(fileContent)
        timeList.extend(searchResult)
timeList=list(set(timeList))

if sys.argv[1] == "view":
    for x in timeList:
        print(int(x) +148* 24*60*60, " ", end="")
    print("\n")
    for t in timeList:
        vTime = time.localtime(int(t))
        print(time.strftime("%Y--%m--%d %H:%M:%S", vTime))

elif sys.argv[1] == "convert":
    # inputArg = [x for x in sys.argv[2:]]
    # print("input ", inputArg)

    for fileName in os.listdir(apiPath):
        filePath = os.path.join(apiPath, fileName)
        with open(filePath, "r", encoding="utf-8") as file:
            fileContent = file.read(-1)
        for raw in timeList:
            fileContent = fileContent.replace(raw, str(int(raw) + +148* 24*60*60))
        with open(filePath, "w+", encoding="utf-8") as file:
            file.write(fileContent)
