# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:54:45 2017

@author: ibrahim
"""

# this added to the script now

from pymongo import MongoClient
import heapq
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def calculateDistance(text,text2):
	result = 0
	for i in range(0,len(text)):
		if (text[i] != '' and text2 != ''):
			result +=  (float(text[i])-float(text2[i]))**2
			#print(str(result)+".......")
	return result/(len(text)-1)	

client = MongoClient('localhost', 27017)
db = client.SearchEngine
test = db.Feature
listresults = []
text_file = test.find_one({"_id": "12"}).get("Histogram")
text = text_file.split('\n')

for i in range(0,20000):
	text_file2 = test.find_one({"_id": str(i)}).get("Histogram")
	text2 = text_file2.split('\n')
	finaleresult = calculateDistance(text,text2)
	listresults.append(finaleresult)
 

imageDiractory = "images1"
print("original image ...")
imginput = mpimg.imread(imageDiractory+'/0/'+'12.jpg')
plt.imshow(imginput)

print(".........................")
#print(im1)
#print(text[1])
#a = [1,2,3]
#b = [2,5,7]

#result = list(np.array(float(text[1]))-np.array(float(text2[1])))
#lestvalue = listresults.index(min(listresults))
#print(min(listresults))


#indice, value = min(enumerate(listresults), key=itemgetter(5))
r = heapq.nsmallest(20, ((k, i) for i, k in enumerate(listresults)))
listresults1 = []
dic = {}
#print(r)
print("the closest 5 images based on the histogram disreptors are ....")
for z in range(0,len(r)):
    rr = str(r[z]).split(',')[1].split(')')
    imageFound = rr[0].split(' ')[1]
    text_file3 = test.find_one({"_id": imageFound}).get("Texture") 
    text3 = text_file2.split('\n')
    finaleresult1 = calculateDistance(text,text3)
    listresults1.append(finaleresult1)
    dic[z]=imageFound

r2 = heapq.nsmallest(10, ((h, p) for p, h in enumerate(listresults1)))
for q in range (0,len(r2)) :  
     rr2 = str(r2[q]).split(',')[1].split(')')
     ima2=rr2[0].split(' ')[1]
     print(ima2)
     h=dic[int(ima2)]
     print(h)
     if (int(h)<10000):
        imginput = mpimg.imread(imageDiractory+'/0/'+h+'.jpg')
     else : 
        imginput = mpimg.imread(imageDiractory+'/1/'+h+'.jpg')
     plt.figure()
     plt.imshow(imginput)
#imginput = mpimg.imread(imageDiractory+'/'+str(listresults.index(min(listresults)))+'.jpg')

#im1 = plt.imshow(imginput)

