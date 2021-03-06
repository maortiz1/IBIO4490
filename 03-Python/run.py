#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:48:12 2019

@author: m_ana
"""

import sys 
import os
import numpy as np
import subprocess
import math
import time

#Importing relevant libraries for code development
start=time.perf_counter();
try:    
    import urllib
except ImportError:
    subprocess.call(['pip3','install','urllib'])
    import urllib

try:    
    import zipfile
except ImportError:
    subprocess.call(['pip','install','zipfile'])
    import zipfile

try:    
    import random
except ImportError:   
    subprocess.call(['pip3','install','random'])
    import random


try:    
    import matplotlib.pyplot as plt
except ImportError:   
    subprocess.call(['pip3','install','--user','matplotlib'])
    import matplotlib.pyplot as plt
    



    


try:    
    import cv2
except ImportError: 
    
    subprocess.call(['pip','install','opencv-python'])
    import cv2
    
try:    
    import math
except ImportError:   
    subprocess.call(['pip','install','math'])
    import math
    
#URL of folder that contains database to be download
URL='https://www.dropbox.com/s/2eg43ogdp7ieb85/blood-cells.zip?dl=1'

print('It will be proceed to download the database')
#checking if databse is already downloaded
if not(os.path.exists('blood-cells.zip')):
    urllib.request.urlretrieve(URL, "blood-cells.zip") 
    print('The database had been download')
else: 
    print('The file blood-cells.zip already exists')
    
print('It will be proceed to decompress de database')
#checkinf if database is already decompress
if not(os.path.exists('blood-cells')):
     zips = zipfile.ZipFile('blood-cells.zip','r')
     zips.extractall('blood-cells')
     zips.close()
    

     
if not(os.path.exists(os.path.join('blood-cells','dataset2-master'))):
     zips = zipfile.ZipFile(os.path.join('blood-cells','dataset2-master.zip'),'r')
     zips.extractall(os.path.join('blood-cells','dataset2-master'))
     zips.close()
     print('The file has finish decompressing')
else:
     print('The file was already decompress')
     
     

#creating path for reading images of database and choosing them
file_path = os.path.join('blood-cells','dataset2-master','dataset2-master','images','TRAIN')
N= int(input("Please enter a multiple of two of the amount of images you will like to visualize: "))
#empty list
allpath = list()
fol=os.listdir(file_path)
a=math.floor(N/2)
fig,axes = plt.subplots(2,a)
plt.axis('off')


for x in range(0,N):
    i = random.randint(0,3)
    pathImg = os.path.join(file_path,fol[i])
    dirList = os.listdir(pathImg)
    j=random.randint(0,len(dirList)-1)
    print('The image: '+dirList[j]+' will be visualize and has the label: '+ fol[i])
    img= cv2.imread(os.path.join(pathImg,dirList[j]))
    img= cv2.putText(img,text=(fol[i]),org=(100,100),fontFace=1, fontScale=2, color=(0,0,0), thickness=2)
    axes[x%2,math.floor(x/2)].imshow(img)
    axes[x%2,math.floor(x/2)].get_xaxis().set_visible(False)
    axes[x%2,math.floor(x/2)].get_yaxis().set_visible(False)
    allpath.append(os.path.join(pathImg,dirList[j]))

endtime = time.perf_counter();
print('The time spent processing this code was: '+ str(endtime-start)+' seconds')
   
cf = plt.get_current_fig_manager()


fig.set_tight_layout({"pad": .0}) 
plt.show()
    

 
    
     



    




