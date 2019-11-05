# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:54:45 2017

@author: ibrahim
"""
from pymongo import MongoClient
import pandas as pd
import numpy as np
import json 
import os


client = MongoClient('localhost', 27017)
db = client.SearchEngine
collection = db.Feature


filediractory = 'features_edgehistogram'
file2 = 'features_homogeneoustexture'
k = 0
for i in range (0,10):
    for j in range (0,10000):
        jasontable = open(filediractory+'/'+str(i)+'/'+str(k)+'.txt','r')
	jasontable1 = open(file2+'/'+str(i)+'/'+str(k)+'.txt','r')
	text = jasontable.read()
	text1 = jasontable1.read()
	dicte = {"_id": str(k),"Histogram": str(text),"Texture":str(text1)}
	print("inserting now...." + str(k))
	post_id = collection.insert_one(dicte).inserted_id
	k+=1
	
	
#post_id = collection.insert_one(dicte).inserted_id
#postedata = collection.insert_one(dicte)
