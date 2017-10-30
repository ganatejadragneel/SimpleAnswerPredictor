import os
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import numpy as np
from functions import sumi,subi,mult,divi,mod
x=input()
maxi=0
index=0
with open('savedData.json') as json_data:
    d=json.load(json_data)
    #print(len(d[0]),len(d[1]))
for i in range(len(d[0])):
    y=fuzz.ratio(x,d[0][i])
    if(y>maxi):
        maxi=y
        index=i
#print(d[0][index],d[1][index])
if(d[1][index]==1):
    y=x.strip().split()
    nums=[]
    for i in range(len(y)):
        if(y[i].isdigit()==1):
            nums.append(int(y[i]))
    print(sumi(nums[0],nums[1]))
elif(d[1][index]==2):
    y=x.strip().split()
    nums=[]
    for i in range(len(y)):
        if(y[i].isdigit()==1):
            nums.append(int(y[i]))
    print(subi(nums[0],nums[1]))
elif(d[1][index]==3):
    y=x.strip().split()
    nums=[]
    for i in range(len(y)):
        if(y[i].isdigit()==1):
            nums.append(int(y[i]))
    print(mult(nums[0],nums[1]))
elif(d[1][index]==4):
    y=x.strip().split()
    nums=[]
    for i in range(len(y)):
        if(y[i].isdigit()==1):
            nums.append(int(y[i]))
    print(divi(nums[0],nums[1]))
elif(d[1][index]==5):
    y=x.strip().split()
    nums=[]
    for i in range(len(y)):
        if(y[i].isdigit()==1):
            nums.append(int(y[i]))
    print(mod(nums[0],nums[1]))
else:
    print("Cant find Solution")
