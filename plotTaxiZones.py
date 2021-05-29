# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:40:31 2021

@author: DELL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import urllib.request
import zipfile
import random
import itertools
import math
import matplotlib as mpl
%matplotlib inline
#%%
import pip
pip.main(['install','ggplot'])
from ggplot import *
#%%
import pandas as pd

from ggplot import *
#%%


#%%read tabels

may2019 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/yellow_tripdata_2019-05.csv")
#%%read taxi zones

taxiZones = pd.read_csv("taxi_zoness.csv")
#%%
del taxiZones["Unnamed: 0"]
del taxiZones["id"]
del taxiZones["order"]
del taxiZones["hole"]
del taxiZones["piece"]
del taxiZones["group"]
del taxiZones["OBJECTID"]
del taxiZones["Shape_Leng"]
del taxiZones["Shape_Area"]
#%%
taxiZones = taxiZones.groupby("LocationID").mean().reset_index()
#%%merging

may2019 = pd.merge(may2019,taxiZones,left_on="PULocationID",right_index=True,how="left")
may2019 = pd.merge(may2019,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%
print(may2019.columns)
#%%clean tabel
del may2019["RatecodeID"]
del may2019["store_and_fwd_flag"]
del may2019["payment_type"]
del may2019["fare_amount"]
del may2019["extra"]
del may2019["mta_tax"]
del may2019["tip_amount"]
del may2019["tolls_amount"]
del may2019["improvement_surcharge"]
del may2019["total_amount"]
del may2019["congestion_surcharge"]
#%%find max and min long1 and long2
maxLong1 = may2019["long_1"].max()
maxLong2 = may2019["long_2"].max()
minLong1 = may2019["long_1"].min()
minLong2 = may2019["long_2"].min()
#%%find max and min lat1 and lat2
maxLat1 = may2019["lat_1"].max()
maxLat2 = may2019["lat_2"].max()
minLat1 = may2019["lat_1"].min()
minLat2 = may2019["lat_2"].min()
#%%
ggplot(may2019) + aes(x = "long_1",y = "lat_1") +
            geom_point(size=0.06) +
            scale_x_continuous(limits=c(minLong1, maxLong1)) +
            scale_y_continuous(limits=c(minLat1, maxLat1))
#%%
plt.figure()
plt.scatter(may2019["long_1"],may2019["lat_1"],color="red")
plt.scatter(may2019["long_2"],may2019["lat_2"],color="blue")
#%%plot on map
BBox = ((may2019.long_1.min(),   may2019.long_1.max(),      
         may2019.lat_1.min(), may2019.lat_1.max()))
#%%read image
ruh_m = plt.imread('nyc.png')
#%%
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(may2019.long_1, may2019.lat_1, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting pickup data on NYC map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
#%%dropoff
BBox = ((may2019.long_2.min(),   may2019.long_2.max(),      
         may2019.lat_2.min(), may2019.lat_2.max()))
#%%
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(may2019.long_1, may2019.lat_1, zorder=1, alpha= 0.2, c='r', s=10)
ax.set_title('Plotting pickup data on NYC map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')