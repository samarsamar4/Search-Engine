import numpy as np
from PIL import Image
from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/Search_pic')
db=client.DB_Search
collection=db.collection_edge

def calculatedistance(pic1,pic2):
    result=float(0)
    for i in range(0,len(pic1)):
        result+=(float(pic1[i])-float(pic2[i]))**2
    return result

index=23
cluster=collection.find_one({"index":index})["cluster"]
cluster_picture_edge=[]
for col in collection.find({"cluster":cluster}):
    cluster_picture_edge.append(col)

similar_picture=[{"result":0,"index":cluster_picture_edge[0]["index"]}]
for k in range(1,len(cluster_picture_edge)):
    result=calculatedistance(cluster_picture_edge[0]["edge_value"],cluster_picture_edge[k]["edge_value"])
    similar_picture.append({"result":result,"index":cluster_picture_edge[k]["index"]})
similar_picture=sorted(similar_picture,key=lambda x:x["result"])
print(similar_picture)

path='/home/ibrahim/Desktop/projet_browser/thumbnails/thumbnails/'
for j in range(0,len(similar_picture)):
    if (j == 20): break
    second = similar_picture[j]["index"] % 10000
    first=int((similar_picture[j]["index"]-second)/10000)
    im=Image.open(path+str(first)+'/'+str(similar_picture[j]["index"])+'.jpg')
    im.show()

