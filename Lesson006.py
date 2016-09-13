# from module import store_spider
#
#
# store_spider('http://movie.douban.com/top250?format=text')
import pandas as pd
import json


# Read lat&lng from file
df = pd.read_csv('file/A0020bl.txt', encoding="shift-jis", sep='\t')
polygons = {}
pots = []
cd = ''

# print(df.ix[3:6, :])
for index, row in df.iterrows():
    # if index <= 100:
    if (row[1] != cd) or (index == len(df)-1):
        polygons[cd] = pots
        cd = row[1]
        pots = []
    else:
        pots.append([row[3], row[2]])
    # else:
    #     break

# print(polygons)
f = open('file/dict.txt', 'w')
writer = json.JSONEncoder()
# print(writer.encode(polygons).strip("{}"))
f.write(writer.encode(polygons).strip("{}"))

