
from sklearn.cluster import KMeans
import numpy as np
from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/Search_pic')
db=client.DB_Search
collection=db.collection_edge

diractory='/home/ibrahim/Desktop/projet_browser'
dir_edge = 'features_edgehistogram'
dir_text = 'features_homogeneoustexture'
table_edge=[]
#DB_text=[]
for i in range(0,40):
	for j in range(0,10000):
		file_edge=open(diractory+dir_edge+'/'+'/'+dir_edge+'/'+str(i)+'/'+str(i*10000+j)+'.txt','r')
		#file_text=open(diractory+dir_text+'/'+'/'+dir_text+'/'+str(i)+'/'+str(i*10000+j)+'.txt','r')
		line_edge=file_edge.read().split()
		#table_text=file_text.read().split()
		table_edge.append(line_edge)
		#DB_text.append(table_text)
	print(i)
array_edge=np.array(table_edge)
Kmeans=KMeans(n_clusters=200).fit(array_edge)
Clusters=Kmeans.predict(array_edge)
for k in range(0,400000):
	cluster=str(Clusters[k])
	line_DB={"index":k,"edge_value":table_edge[k],"cluster":cluster}
	collection.insert_one(line_DB)
# testfile=open(diractory+dir_edge+'/'+'/'+dir_edge+'/'+str(5)+'/'+str(5*10000+0)+'.txt','r')
# tabletest=testfile.read().split()
# DB_test=[]
# for i in range(0,50000):
# 	DB_test.append(tabletest)
# arraytest=np.array(DB_test)
# print(Kmeans.predict(arraytest))



