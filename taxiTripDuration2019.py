# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:06:30 2021

@author: Aleksandra Mitro
Statistical analysis of duration of taxi rides in seconds
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%Read tabels for may 2019
yellowMay2019 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/yellow_tripdata_2019-05.csv")
greenMay2019 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/green_tripdata_2019-05.csv")

#%%Read tabels for july

yellowJuly2019 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/yellow_tripdata_2019-07.csv")
greenJuly2019 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/green_tripdata_2019-07.csv")

#%%Read tabels for november

yellowNovember2019 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/yellow_tripdata_2019-11.csv")
greenNovember2019 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/green_tripdata_2019-11.csv")
#%%Clean data
yellowMay2019["pickup_date"] = yellowMay2019["tpep_pickup_datetime"].str[0:10]
yellowMay2019 = yellowMay2019[("2019-05-01"<=yellowMay2019["pickup_date"])&(yellowMay2019["pickup_date"]<="2019-05-31")]
greenMay2019["pickup_date"] = greenMay2019["lpep_pickup_datetime"].str[0:10]
greenMay2019 = greenMay2019[("2019-05-01"<=greenMay2019["pickup_date"])&(greenMay2019["pickup_date"]<="2019-05-31")]
yellowJuly2019["pickup_date"] = yellowJuly2019["tpep_pickup_datetime"].str[0:10]
yellowJuly2019 = yellowJuly2019[("2019-07-01"<=yellowJuly2019["pickup_date"])&(yellowJuly2019["pickup_date"]<="2019-07-31")]
greenJuly2019["pickup_date"] = greenJuly2019["lpep_pickup_datetime"].str[0:10]
greenJuly2019 = greenJuly2019[("2019-07-01"<=greenJuly2019["pickup_date"])&(greenJuly2019["pickup_date"]<="2019-07-31")]
yellowNovember2019["pickup_date"] = yellowNovember2019["tpep_pickup_datetime"].str[0:10]
yellowNovember2019 = yellowNovember2019[("2019-11-01"<=yellowNovember2019["pickup_date"])&(yellowNovember2019["pickup_date"]<="2019-11-31")]
greenNovember2019["pickup_date"] = greenNovember2019["lpep_pickup_datetime"].str[0:10]
greenNovember2019 = greenNovember2019[("2019-11-01"<=greenNovember2019["pickup_date"])&(greenNovember2019["pickup_date"]<="2019-11-31")]
#%%Adding dropoff date
yellowMay2019["dropoff_date"] = yellowMay2019["tpep_dropoff_datetime"].str[0:10]
yellowJuly2019["dropoff_date"] = yellowJuly2019["tpep_dropoff_datetime"].str[0:10]
yellowNovember2019["dropoff_date"] = yellowNovember2019["tpep_dropoff_datetime"].str[0:10]
greenMay2019["dropoff_date"] = greenMay2019["lpep_dropoff_datetime"].str[0:10]
greenJuly2019["dropoff_date"] = greenJuly2019["lpep_dropoff_datetime"].str[0:10]
greenNovember2019["dropoff_date"] = greenNovember2019["lpep_dropoff_datetime"].str[0:10]
#%%Filter rides that has same date for pickup and dropoff
sameDayYellowMay = yellowMay2019[yellowMay2019["pickup_date"] == yellowMay2019["dropoff_date"]]
sameDayGreenMay = greenMay2019[greenMay2019["pickup_date"] == greenMay2019["dropoff_date"]]
sameDayYellowJuly = yellowJuly2019[yellowJuly2019["pickup_date"] == yellowJuly2019["dropoff_date"]]
sameDayGreenJuly = greenJuly2019[greenJuly2019["pickup_date"] == greenJuly2019["dropoff_date"]]
sameDayYellowNovember = yellowNovember2019[yellowNovember2019["pickup_date"] == yellowNovember2019["dropoff_date"]]
sameDayGreenNovember = greenNovember2019[greenNovember2019["pickup_date"] == greenNovember2019["dropoff_date"]]
#%% ---- Computing duration for each ride in seconds ----
#%%Yellow May 2019
sameDayYellowMay["start_sec"] = sameDayYellowMay["tpep_pickup_datetime"].str[11:13].astype("int")*60*60 + sameDayYellowMay["tpep_pickup_datetime"].str[14:16].astype("int")*60 + sameDayYellowMay["tpep_pickup_datetime"].str[17:19].astype("int")
sameDayYellowMay["end_sec"] = sameDayYellowMay["tpep_dropoff_datetime"].str[11:13].astype("int")*60*60 + sameDayYellowMay["tpep_dropoff_datetime"].str[14:16].astype("int")*60 + sameDayYellowMay["tpep_dropoff_datetime"].str[17:19].astype("int")
sameDayYellowMay["duration_sec"] = sameDayYellowMay["end_sec"] - sameDayYellowMay["start_sec"]
#%%Yellow July 2019
sameDayYellowJuly["start_sec"] = sameDayYellowJuly["tpep_pickup_datetime"].str[11:13].astype("int")*60*60 + sameDayYellowJuly["tpep_pickup_datetime"].str[14:16].astype("int")*60 + sameDayYellowJuly["tpep_pickup_datetime"].str[17:19].astype("int")
sameDayYellowJuly["end_sec"] = sameDayYellowJuly["tpep_dropoff_datetime"].str[11:13].astype("int")*60*60 + sameDayYellowJuly["tpep_dropoff_datetime"].str[14:16].astype("int")*60 + sameDayYellowJuly["tpep_dropoff_datetime"].str[17:19].astype("int")
sameDayYellowJuly["duration_sec"] = sameDayYellowJuly["end_sec"] - sameDayYellowJuly["start_sec"]
#%%Yellow November 2019
sameDayYellowNovember["start_sec"] = sameDayYellowNovember["tpep_pickup_datetime"].str[11:13].astype("int")*60*60 + sameDayYellowNovember["tpep_pickup_datetime"].str[14:16].astype("int")*60 + sameDayYellowNovember["tpep_pickup_datetime"].str[17:19].astype("int")
sameDayYellowNovember["end_sec"] = sameDayYellowNovember["tpep_dropoff_datetime"].str[11:13].astype("int")*60*60 + sameDayYellowNovember["tpep_dropoff_datetime"].str[14:16].astype("int")*60 + sameDayYellowNovember["tpep_dropoff_datetime"].str[17:19].astype("int")
sameDayYellowNovember["duration_sec"] = sameDayYellowNovember["end_sec"] - sameDayYellowNovember["start_sec"]
#%%Green May 2019
sameDayGreenMay["start_sec"] = sameDayGreenMay["lpep_pickup_datetime"].str[11:13].astype("int")*60*60 + sameDayGreenMay["lpep_pickup_datetime"].str[14:16].astype("int")*60 + sameDayGreenMay["lpep_pickup_datetime"].str[17:19].astype("int")
sameDayGreenMay["end_sec"] = sameDayGreenMay["lpep_dropoff_datetime"].str[11:13].astype("int")*60*60 + sameDayGreenMay["lpep_dropoff_datetime"].str[14:16].astype("int")*60 + sameDayGreenMay["lpep_dropoff_datetime"].str[17:19].astype("int")
sameDayGreenMay["duration_sec"] = sameDayGreenMay["end_sec"] - sameDayGreenMay["start_sec"]
#%%Green July 2019
sameDayGreenJuly["start_sec"] = sameDayGreenJuly["lpep_pickup_datetime"].str[11:13].astype("int")*60*60 + sameDayGreenJuly["lpep_pickup_datetime"].str[14:16].astype("int")*60 + sameDayGreenJuly["lpep_pickup_datetime"].str[17:19].astype("int")
sameDayGreenJuly["end_sec"] = sameDayGreenJuly["lpep_dropoff_datetime"].str[11:13].astype("int")*60*60 + sameDayGreenJuly["lpep_dropoff_datetime"].str[14:16].astype("int")*60 + sameDayGreenJuly["lpep_dropoff_datetime"].str[17:19].astype("int")
sameDayGreenJuly["duration_sec"] = sameDayGreenJuly["end_sec"] - sameDayGreenJuly["start_sec"]
#%%Green November 2019
sameDayGreenNovember["start_sec"] = sameDayGreenNovember["lpep_pickup_datetime"].str[11:13].astype("int")*60*60 + sameDayGreenNovember["lpep_pickup_datetime"].str[14:16].astype("int")*60 + sameDayGreenNovember["lpep_pickup_datetime"].str[17:19].astype("int")
sameDayGreenNovember["end_sec"] = sameDayGreenNovember["lpep_dropoff_datetime"].str[11:13].astype("int")*60*60 + sameDayGreenNovember["lpep_dropoff_datetime"].str[14:16].astype("int")*60 + sameDayGreenNovember["lpep_dropoff_datetime"].str[17:19].astype("int")
sameDayGreenNovember["duration_sec"] = sameDayGreenNovember["end_sec"] - sameDayGreenNovember["start_sec"]
#%%Clean rides shorter than 2 minutes
sameDayYellowMay = sameDayYellowMay[sameDayYellowMay["duration_sec"]>120]
sameDayYellowJuly = sameDayYellowJuly[sameDayYellowJuly["duration_sec"]>120]
sameDayYellowNovember = sameDayYellowNovember[sameDayYellowNovember["duration_sec"]>120]
sameDayGreenMay = sameDayGreenMay[sameDayGreenMay["duration_sec"]>120]
sameDayGreenJuly = sameDayGreenJuly[sameDayGreenJuly["duration_sec"]>120]
sameDayGreenNovember = sameDayGreenNovember[sameDayGreenNovember["duration_sec"]>120]
#%%Average trip duration in minutes
print(sameDayYellowMay["duration_sec"].mean()/60)
print(sameDayGreenMay["duration_sec"].mean()/60)
print(sameDayYellowJuly["duration_sec"].mean()/60)
print(sameDayGreenJuly["duration_sec"].mean()/60)
print(sameDayYellowNovember["duration_sec"].mean()/60)
print(sameDayGreenNovember["duration_sec"].mean()/60)
#%%Histogram of rides in minutes(Yellow taxi may 2019)
sdym = sameDayYellowMay[sameDayYellowMay["duration_sec"]<=1800]
#%%
plt.plot()
plt.hist(sdym["duration_sec"]/60,bins=20,edgecolor="orange",color="yellow")
plt.xlabel("Minutes")
plt.ylabel("Number of rides")
plt.title("Yellow taxi may 2019")
#%%Histogram of rides in minutes(Yellow taxi july 2019)
sdyj = sameDayYellowJuly[sameDayYellowJuly["duration_sec"]<=1800]
#%%
plt.plot()
plt.hist(sdyj["duration_sec"]/60,bins=20,edgecolor="orange",color="yellow")
plt.xlabel("Minutes")
plt.ylabel("Number of rides")
plt.title("Yellow taxi july 2019")
#%%Histogram of rides in minutes(Yellow taxi july 2019)
sdyn = sameDayYellowNovember[sameDayYellowNovember["duration_sec"]<=1800]
#%%
plt.plot()
plt.hist(sdyn["duration_sec"]/60,bins=20,edgecolor="orange",color="yellow")
plt.xlabel("Minutes")
plt.ylabel("Number of rides")
plt.title("Yellow taxi november 2019")
#%%Histogram of rides in minutes(Green taxi may 2019)
sdgm = sameDayGreenMay[sameDayGreenMay["duration_sec"]<=1800]
#%%
plt.plot()
plt.hist(sdgm["duration_sec"]/60,bins=20,edgecolor="blue",color="green")
plt.xlabel("Minutes")
plt.ylabel("Number of rides")
plt.title("Green taxi may 2019")
#%%Histogram of rides in minutes(Green taxi july 2019)
sdgj = sameDayGreenJuly[sameDayGreenJuly["duration_sec"]<=1800]
#%%
plt.plot()
plt.hist(sdgj["duration_sec"]/60,bins=20,edgecolor="blue",color="green")
plt.xlabel("Minutes")
plt.ylabel("Number of rides")
plt.title("Green taxi july 2019")
#%%Histogram of rides in minutes(Green taxi july 2019)
sdgn = sameDayGreenNovember[sameDayGreenNovember["duration_sec"]<=1800]
#%%
plt.plot()
plt.hist(sdgn["duration_sec"]/60,bins=20,edgecolor="blue",color="green")
plt.xlabel("Minutes")
plt.ylabel("Number of rides")
plt.title("Green taxi november 2019")
#%%Read taxi zones
taxiZones = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/taxi_zones.csv")
#%%Clean data
del taxiZones["the_geom"]
del taxiZones["Shape_Leng"]
del taxiZones["Shape_Area"]
#%%Average duration of ride to JFK airport for Yellow Taxi
jfkM = sameDayYellowMay[sameDayYellowMay["RatecodeID"] == 2]
jfkY = sameDayYellowJuly[sameDayYellowJuly["RatecodeID"] == 2]
jfkN = sameDayYellowNovember[sameDayYellowNovember["RatecodeID"] == 2]

#%%
print(jfkM["duration_sec"].mean()/60)
print(jfkY["duration_sec"].mean()/60)
print(jfkN["duration_sec"].mean()/60)
#%%Average duration of ride to Newark airport for Yellow Taxi
newM = sameDayYellowMay[sameDayYellowMay["RatecodeID"] == 3]
newY = sameDayYellowJuly[sameDayYellowJuly["RatecodeID"] == 3]
newN = sameDayYellowNovember[sameDayYellowNovember["RatecodeID"] == 3]
#%%
print(newM["duration_sec"].mean()/60)
print(newY["duration_sec"].mean()/60)
print(newN["duration_sec"].mean()/60)

#%% ---- Merge with taxi zones ----
#%%Green taxi may
sameDayGreenMayZones = pd.merge(sameDayGreenMay,taxiZones,left_on="PULocationID",right_index = True,how="left")
sameDayGreenMayZones = pd.merge(sameDayGreenMayZones,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Green taxi july
sameDayGreenJulyZones = pd.merge(sameDayGreenJuly,taxiZones,left_on="PULocationID",right_index = True,how="left")
sameDayGreenJulyZones = pd.merge(sameDayGreenJulyZones,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Green taxi november
sameDayGreenNovemberZones = pd.merge(sameDayGreenNovember,taxiZones,left_on="PULocationID",right_index = True,how="left")
sameDayGreenNovemberZones = pd.merge(sameDayGreenNovemberZones,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Yellow taxi may
sameDayYellowMayZones = pd.merge(sameDayYellowMay,taxiZones,left_on="PULocationID",right_index = True,how="left")
sameDayYellowMayZones = pd.merge(sameDayYellowMayZones,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Yellow taxi july
sameDayYellowJulyZones = pd.merge(sameDayYellowJuly,taxiZones,left_on="PULocationID",right_index = True,how="left")
sameDayYellowJulyZones = pd.merge(sameDayYellowJulyZones,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Yellow taxi november
sameDayYellowNovemberZones = pd.merge(sameDayYellowNovember,taxiZones,left_on="PULocationID",right_index = True,how="left")
sameDayYellowNovemberZones = pd.merge(sameDayYellowNovemberZones,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Average duration in minutes for each zone may
gbzym = sameDayYellowMayZones.groupby("borough_1")["duration_sec"].mean()/60
gbzgm = sameDayGreenMayZones.groupby("borough_1")["duration_sec"].mean()/60
plt.figure()
plt.plot(gbzym.index,gbzym.values,color="yellow",label="Yellow taxi")
plt.plot(gbzgm.index,gbzgm.values,color="green",label="Green taxi")
plt.title("Average duration in minutes for each zone in may")
plt.xlabel("Zone")
plt.ylabel("Minutes")
plt.legend(loc="best")
#%%Average duration in minutes for each zone july
gbzyj = sameDayYellowJulyZones.groupby("borough_1")["duration_sec"].mean()/60
gbzgj = sameDayGreenJulyZones.groupby("borough_1")["duration_sec"].mean()/60
plt.figure()
plt.plot(gbzyj.index,gbzyj.values,color="yellow",label="Yellow taxi")
plt.plot(gbzgj.index,gbzgj.values,color="green",label="Green taxi")
plt.title("Average duration in minutes for each zone in july")
plt.xlabel("Zone")
plt.ylabel("Minutes")
plt.legend(loc="best")
#%%Average duration in minutes for each zone november
gbzyn = sameDayYellowNovemberZones.groupby("borough_1")["duration_sec"].mean()/60
gbzgn = sameDayGreenNovemberZones.groupby("borough_1")["duration_sec"].mean()/60
plt.figure()
plt.plot(gbzyn.index,gbzyn.values,color="yellow",label="Yellow taxi")
plt.plot(gbzgn.index,gbzgn.values,color="green",label="Green taxi")
plt.title("Average duration in minutes for each zone in november")
plt.xlabel("Zone")
plt.ylabel("Minutes")
plt.legend(loc="best")
#%%Difference between average duration for pickup and dropoff zones may 2019
gbzym = sameDayYellowMayZones.groupby("borough_1")["duration_sec"].mean()/60
gbzym2 = sameDayYellowMayZones.groupby("borough_2")["duration_sec"].mean()/60
gbzgm = sameDayGreenMayZones.groupby("borough_1")["duration_sec"].mean()/60
gbzgm2 = sameDayGreenMayZones.groupby("borough_2")["duration_sec"].mean()/60
plt.figure()
plt.plot(gbzym.index,gbzym.values,color="blue",label="Pickup yellow")
plt.plot(gbzym2.index,gbzym2.values,color="red",label="Dropoff yellow")
plt.plot(gbzgm.index,gbzgm.values,color="blue",label="Pickup green",linestyle="--")
plt.plot(gbzgm2.index,gbzgm2.values,color="red",label="Dropoff green",linestyle="--")
plt.xlabel("Zone")
plt.ylabel("Minutes")
plt.legend(loc="best")
plt.title("Difference between average duration for pickup and dropoff zones may 2019")
#%%Difference between average duration for pickup and dropoff zones july 2019
gbzyj = sameDayYellowJulyZones.groupby("borough_1")["duration_sec"].mean()/60
gbzyj2 = sameDayYellowJulyZones.groupby("borough_2")["duration_sec"].mean()/60
gbzgj = sameDayGreenJulyZones.groupby("borough_1")["duration_sec"].mean()/60
gbzgj2 = sameDayGreenJulyZones.groupby("borough_2")["duration_sec"].mean()/60
plt.figure()
plt.plot(gbzyj.index,gbzyj.values,color="blue",label="Pickup yellow")
plt.plot(gbzyj2.index,gbzyj2.values,color="red",label="Dropoff yellow")
plt.plot(gbzgj.index,gbzgj.values,color="blue",label="Pickup green",linestyle="--")
plt.plot(gbzgj2.index,gbzgj2.values,color="red",label="Dropoff green",linestyle="--")
plt.xlabel("Zone")
plt.ylabel("Minutes")
plt.legend(loc="best")
plt.title("Difference between average duration for pickup and dropoff zones july 2019")
#%%Difference between average duration for pickup and dropoff zones november 2019
gbzyn = sameDayYellowNovemberZones.groupby("borough_1")["duration_sec"].mean()/60
gbzyn2 = sameDayYellowNovemberZones.groupby("borough_2")["duration_sec"].mean()/60
gbzgn = sameDayGreenNovemberZones.groupby("borough_1")["duration_sec"].mean()/60
gbzgn2 = sameDayGreenNovemberZones.groupby("borough_2")["duration_sec"].mean()/60
plt.figure()
plt.plot(gbzyn.index,gbzyn.values,color="blue",label="Pickup yellow")
plt.plot(gbzyn2.index,gbzyn2.values,color="red",label="Dropoff yellow")
plt.plot(gbzgn.index,gbzgn.values,color="blue",label="Pickup green",linestyle="--")
plt.plot(gbzgn2.index,gbzgn2.values,color="red",label="Dropoff green",linestyle="--")
plt.xlabel("Zone")
plt.ylabel("Minutes")
plt.legend(loc="best")
plt.title("Difference between average duration for pickup and dropoff zones november 2019")
#%%How much time newyorkers spend in yellow taxi for each day
gbdYM = sameDayYellowMayZones.groupby("pickup_date")["duration_sec"].mean() 
gbdYJ = sameDayYellowJulyZones.groupby("pickup_date")["duration_sec"].mean()
gbdYN = sameDayYellowNovemberZones.groupby("pickup_date")["duration_sec"].mean()
#%%plot
plt.figure()
plt.plot(np.arange(1,32),gbdYM.values/60,label="May",color="green")
plt.plot(np.arange(1,32),gbdYJ.values/60,label="July",color="red",linestyle="--")
plt.plot(np.arange(1,31),gbdYN.values/60,label="November",color="blue",linestyle=":")
plt.legend(loc="best")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.title("Average time in taxi Yellow taxi 2019")
#%%How much time newyorkers spend in green taxi for each day
gbdGM = sameDayGreenMayZones.groupby("pickup_date")["duration_sec"].mean() 
gbdGJ = sameDayGreenJulyZones.groupby("pickup_date")["duration_sec"].mean()
gbdGN = sameDayGreenNovemberZones.groupby("pickup_date")["duration_sec"].mean()
#%%plot
plt.figure()
plt.plot(np.arange(1,32),gbdGM.values/60,label="May",color="green")
plt.plot(np.arange(1,32),gbdGJ.values/60,label="July",color="red",linestyle="--")
plt.plot(np.arange(1,31),gbdGN.values/60,label="November",color="blue",linestyle=":")
plt.legend(loc="best")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.title("Average time in taxi Green taxi 2019")
#%%How much time newyorkers spend in yellow taxi in days
print(sameDayYellowMayZones["duration_sec"].sum()/86400)
print(sameDayYellowJulyZones["duration_sec"].sum()/86400)
print(sameDayYellowNovemberZones["duration_sec"].sum()/86400)
#%%How much time newyorkers spend in green taxi in days
print(sameDayGreenMayZones["duration_sec"].sum()/86400)
print(sameDayGreenJulyZones["duration_sec"].sum()/86400)
print(sameDayGreenNovemberZones["duration_sec"].sum()/86400)
#%%Average duration in each pickup hour Yellow taxi 2019
gbyHYM = sameDayYellowMayZones.groupby(sameDayYellowMayZones["tpep_pickup_datetime"].str[11:13].astype("int"))["duration_sec"].mean()
gbyHYJ = sameDayYellowJulyZones.groupby(sameDayYellowMayZones["tpep_pickup_datetime"].str[11:13].astype("int"))["duration_sec"].mean()
gbyHYN = sameDayYellowNovemberZones.groupby(sameDayYellowMayZones["tpep_pickup_datetime"].str[11:13].astype("int"))["duration_sec"].mean()
#%%
plt.figure()
plt.plot(gbyHYM.index,gbyHYM.values/60,color="green",label="May")
plt.plot(gbyHYJ.index,gbyHYJ.values/60,color="red",label="July")
plt.plot(gbyHYN.index,gbyHYN.values/60,color="blue",label="November")
plt.legend(loc="best")
plt.xlabel("Hour")
plt.ylabel("Minutes")
plt.title("Average time spent in taxi for each hour (Yellow taxi 2019)")
#%%Average duration in each pickup hour Green taxi 2019
gbyHGM = sameDayGreenMayZones.groupby(sameDayGreenMayZones["lpep_pickup_datetime"].str[11:13].astype("int"))["duration_sec"].mean()
gbyHGJ = sameDayGreenJulyZones.groupby(sameDayGreenMayZones["lpep_pickup_datetime"].str[11:13].astype("int"))["duration_sec"].mean()
gbyHGN = sameDayGreenNovemberZones.groupby(sameDayGreenMayZones["lpep_pickup_datetime"].str[11:13].astype("int"))["duration_sec"].mean()
#%%
plt.figure()
plt.plot(gbyHGM.index,gbyHGM.values/60,color="green",label="May")
plt.plot(gbyHGJ.index,gbyHGJ.values/60,color="red",label="July")
plt.plot(gbyHGN.index,gbyHGN.values/60,color="blue",label="November")
plt.legend(loc="best")
plt.xlabel("Hour")
plt.ylabel("Minutes")
plt.title("Average time spent in taxi for each hour (Green taxi 2019)")
#%%Average speed by pickup borough
boroughSpeedYM = sameDayYellowMayZones.groupby(['borough_1'])['duration_sec', 'trip_distance'].sum().reset_index()
boroughSpeedYM['mph'] = 3600 * (boroughSpeedYM.trip_distance / boroughSpeedYM.duration_sec)
boroughSpeedYJ = sameDayYellowJulyZones.groupby(['borough_1'])['duration_sec', 'trip_distance'].sum().reset_index()
boroughSpeedYJ['mph'] = 3600 * (boroughSpeedYJ.trip_distance / boroughSpeedYJ.duration_sec)
boroughSpeedYN = sameDayYellowNovemberZones.groupby(['borough_1'])['duration_sec', 'trip_distance'].sum().reset_index()
boroughSpeedYN['mph'] = 3600 * (boroughSpeedYN.trip_distance / boroughSpeedYN.duration_sec)
#%%plot
plt.figure()
plt.plot(boroughSpeedYM["borough_1"],boroughSpeedYM["mph"],label="May")
plt.plot(boroughSpeedYJ["borough_1"],boroughSpeedYJ["mph"],label="July")
plt.plot(boroughSpeedYN["borough_1"],boroughSpeedYN["mph"],label="November")
plt.legend(loc="best")
plt.xlabel("Pickup borough")
plt.ylabel("Speed in mph")
plt.title("Average speed in each borough (Yellow taxi 2019)")
#%%
boroughSpeedGM = sameDayGreenMayZones.groupby(['borough_1'])['duration_sec', 'trip_distance'].sum().reset_index()
boroughSpeedGM['mph'] = 3600 * (boroughSpeedGM.trip_distance / boroughSpeedGM.duration_sec)
boroughSpeedGJ = sameDayGreenJulyZones.groupby(['borough_1'])['duration_sec', 'trip_distance'].sum().reset_index()
boroughSpeedGJ['mph'] = 3600 * (boroughSpeedGJ.trip_distance / boroughSpeedGJ.duration_sec)
boroughSpeedGN = sameDayGreenNovemberZones.groupby(['borough_1'])['duration_sec', 'trip_distance'].sum().reset_index()
boroughSpeedGN['mph'] = 3600 * (boroughSpeedGN.trip_distance / boroughSpeedGN.duration_sec)
#%%plot
plt.figure()
plt.plot(boroughSpeedGM["borough_1"],boroughSpeedGM["mph"],label="May")
plt.plot(boroughSpeedGJ["borough_1"],boroughSpeedGJ["mph"],label="July")
plt.plot(boroughSpeedGN["borough_1"],boroughSpeedGN["mph"],label="November")
plt.legend(loc="best")
plt.xlabel("Pickup borough")
plt.ylabel("Speed in mph")
plt.title("Average speed in each borough (Green taxi 2019)")
#%%Average speed by pickup date yellow taxi 2019
dateSpeedYM = sameDayYellowMayZones.groupby(sameDayYellowMayZones['pickup_date'].str[8:10].astype("int"))["duration_sec", "trip_distance"].sum().reset_index()
dateSpeedYM['mph'] = 3600 * (dateSpeedYM.trip_distance / dateSpeedYM.duration_sec)
dateSpeedYJ = sameDayYellowJulyZones.groupby(sameDayYellowJulyZones['pickup_date'].str[8:10].astype("int"))['duration_sec', 'trip_distance'].sum().reset_index()
dateSpeedYJ['mph'] = 3600 * (dateSpeedYJ.trip_distance / dateSpeedYJ.duration_sec)
dateSpeedYN = sameDayYellowNovemberZones.groupby(sameDayYellowNovemberZones['pickup_date'].str[8:10].astype("int"))['duration_sec', 'trip_distance'].sum().reset_index()
dateSpeedYN['mph'] = 3600 * (dateSpeedYN.trip_distance / dateSpeedYN.duration_sec)
#%%plot
plt.figure()
plt.plot(dateSpeedYM["pickup_date"],dateSpeedYM["mph"],label="May")
plt.plot(dateSpeedYJ["pickup_date"],dateSpeedYJ["mph"],label="July")
plt.plot(dateSpeedYN["pickup_date"],dateSpeedYN["mph"],label="November")
plt.legend(loc="best")
plt.xlabel("Hour")
plt.ylabel("Speed in mph")
plt.title("Average speed in each hour (Yellow taxi 2019)")
#%%Average speed by pickup date green taxi 2019
dateSpeedGM = sameDayGreenMayZones.groupby(sameDayGreenMayZones['pickup_date'].str[8:10].astype("int"))["duration_sec", "trip_distance"].sum().reset_index()
dateSpeedGM['mph'] = 3600 * (dateSpeedGM.trip_distance / dateSpeedGM.duration_sec)
dateSpeedGJ = sameDayGreenJulyZones.groupby(sameDayGreenJulyZones['pickup_date'].str[8:10].astype("int"))['duration_sec', 'trip_distance'].sum().reset_index()
dateSpeedGJ['mph'] = 3600 * (dateSpeedGJ.trip_distance / dateSpeedGJ.duration_sec)
dateSpeedGN = sameDayGreenNovemberZones.groupby(sameDayGreenNovemberZones['pickup_date'].str[8:10].astype("int"))['duration_sec', 'trip_distance'].sum().reset_index()
dateSpeedGN['mph'] = 3600 * (dateSpeedGN.trip_distance / dateSpeedGN.duration_sec)
#%%plot
plt.figure()
plt.plot(dateSpeedGM["pickup_date"],dateSpeedGM["mph"],label="May")
plt.plot(dateSpeedGJ["pickup_date"],dateSpeedGJ["mph"],label="July")
plt.plot(dateSpeedGN["pickup_date"],dateSpeedGN["mph"],label="November")
plt.legend(loc="best")
plt.xlabel("Hour")
plt.ylabel("Speed in mph")
plt.title("Average speed in each hour (Green taxi 2019)")
#%%Add days to dataFrame green taxi
sameDayGreenMayZones['inputDate'] = pd.to_datetime(sameDayGreenMayZones['pickup_date'])
sameDayGreenMayZones['dayOfWeek'] = sameDayGreenMayZones['inputDate'].dt.day_name()
sameDayGreenJulyZones['inputDate'] = pd.to_datetime(sameDayGreenJulyZones['pickup_date'])
sameDayGreenJulyZones['dayOfWeek'] = sameDayGreenJulyZones['inputDate'].dt.day_name()
sameDayGreenNovemberZones['inputDate'] = pd.to_datetime(sameDayGreenNovemberZones['pickup_date'])
sameDayGreenNovemberZones['dayOfWeek'] = sameDayGreenNovemberZones['inputDate'].dt.day_name()
#%%Add days to dataFrame yellow taxi
sameDayYellowMayZones['inputDate'] = pd.to_datetime(sameDayYellowMayZones['pickup_date'])
sameDayYellowMayZones['dayOfWeek'] = sameDayYellowMayZones['inputDate'].dt.day_name()
sameDayYellowJulyZones['inputDate'] = pd.to_datetime(sameDayYellowJulyZones['pickup_date'])
sameDayYellowJulyZones['dayOfWeek'] = sameDayYellowJulyZones['inputDate'].dt.day_name()
sameDayYellowNovemberZones['inputDate'] = pd.to_datetime(sameDayYellowNovemberZones['pickup_date'])
sameDayYellowNovemberZones['dayOfWeek'] = sameDayYellowNovemberZones['inputDate'].dt.day_name()
#%%Group rides by day of week
groupDayYM = sameDayYellowMayZones.groupby("dayOfWeek")
groupDayYJ = sameDayYellowJulyZones.groupby("dayOfWeek")
groupDayYN = sameDayYellowNovemberZones.groupby("dayOfWeek")
groupDayGM = sameDayGreenMayZones.groupby("dayOfWeek")
groupDayGJ = sameDayGreenJulyZones.groupby("dayOfWeek")
groupDayGN = sameDayGreenNovemberZones.groupby("dayOfWeek")
#%%Number of rides for each day yellow 2019
gdnYM = groupDayYM["VendorID"].count().reset_index()
gdnYJ = groupDayYJ["VendorID"].count().reset_index()
gdnYN = groupDayYN["VendorID"].count().reset_index()
#%%plot
plt.figure()
plt.plot(gdnYM.dayOfWeek,gdnYM.VendorID,label="May",color="green")
plt.plot(gdnYJ.dayOfWeek,gdnYJ.VendorID,label="July",color="red")
plt.plot(gdnYN.dayOfWeek,gdnYN.VendorID,label="November",color="blue")
plt.legend(loc="best")
plt.xlabel("Day of week")
plt.ylabel("Number of rides")
plt.title("Number of rides for each day in week (Yellow taxi 2019)")
#%%Number of rides for each day yellow 2019
gdnGM = groupDayGM["VendorID"].count().reset_index()
gdnGJ = groupDayGJ["VendorID"].count().reset_index()
gdnGN = groupDayGN["VendorID"].count().reset_index()
#%%plot
plt.figure()
plt.plot(gdnGM.dayOfWeek,gdnGM.VendorID,label="May",color="green")
plt.plot(gdnGJ.dayOfWeek,gdnGJ.VendorID,label="July",color="red")
plt.plot(gdnGN.dayOfWeek,gdnGN.VendorID,label="November",color="blue")
plt.legend(loc="best")
plt.xlabel("Day of week")
plt.ylabel("Number of rides")
plt.title("Number of rides for each day in week (Green taxi 2019)")
#%% ----Next analysis will be only for yellow taxi----
#%%Average trip duration for each day in week
gddYM = groupDayYM["duration_sec"].mean().reset_index()
gddYJ = groupDayYJ["duration_sec"].mean().reset_index()
gddYN = groupDayYN["duration_sec"].mean().reset_index()
#%%
plt.figure()
plt.plot(gddYM.dayOfWeek,gddYM.duration_sec/60,label="May",color="green")
plt.plot(gddYJ.dayOfWeek,gddYJ.duration_sec/60,label="July",color="red")
plt.plot(gddYN.dayOfWeek,gddYN.duration_sec/60,label="November",color="blue")
plt.legend(loc="best")
plt.xlabel("Day of week")
plt.ylabel("Minutes")
plt.title("Average ride duration for each day in week (Yellow taxi 2019)")
#%%Number of passengers for each day in week
gdpYM = groupDayYM["passenger_count"].sum().reset_index()
gdpYJ = groupDayYJ["passenger_count"].sum().reset_index()
gdpYN = groupDayYN["passenger_count"].sum().reset_index()
#%%plot
plt.figure()
plt.plot(gdpYM.dayOfWeek,gdpYM.passenger_count,label="May",color="green")
plt.plot(gdpYJ.dayOfWeek,gdpYJ.passenger_count,label="July",color="red")
plt.plot(gdpYN.dayOfWeek,gdpYN.passenger_count,label="November",color="blue")
plt.legend(loc="best")
plt.xlabel("Number of passengers")
plt.ylabel("Minutes")
plt.title("Number of passengers for each day in week (Yellow taxi 2019)")
#%%Group by pickup borough yellow taxi
gdbYM = sameDayYellowMayZones.groupby(["dayOfWeek","borough_1"])["VendorID"].count().reset_index()
gdbYJ = sameDayYellowJulyZones.groupby(["dayOfWeek","borough_1"])["VendorID"].count().reset_index()
gdbYN = sameDayYellowNovemberZones.groupby(["dayOfWeek","borough_1"])["VendorID"].count().reset_index()
#%%Find max and min
print("Maximum")
mm = gdbYM["VendorID"].max()
my = gdbYJ["VendorID"].max()
mn = gdbYN["VendorID"].max()
print(gdbYM[gdbYM["VendorID"] == mm])
print(gdbYJ[gdbYJ["VendorID"] == my])
print(gdbYN[gdbYN["VendorID"] == mn])
print("Minimum")
mm = gdbYM["VendorID"].min()
my = gdbYJ["VendorID"].min()
mn = gdbYN["VendorID"].min()
print(gdbYM[gdbYM["VendorID"] == mm])
print(gdbYJ[gdbYJ["VendorID"] == my])
print(gdbYN[gdbYN["VendorID"] == mn])
#%%Group by pickup borough green taxi
gdbGM = sameDayGreenMayZones.groupby(["dayOfWeek","borough_1"])["VendorID"].count().reset_index()
gdbGJ = sameDayGreenJulyZones.groupby(["dayOfWeek","borough_1"])["VendorID"].count().reset_index()
gdbGN = sameDayGreenNovemberZones.groupby(["dayOfWeek","borough_1"])["VendorID"].count().reset_index()
#%%Find max and min
print("Maximum")
mm = gdbGM["VendorID"].max()
my = gdbGJ["VendorID"].max()
mn = gdbGN["VendorID"].max()
print(gdbGM[gdbGM["VendorID"] == mm])
print(gdbGJ[gdbGJ["VendorID"] == my])
print(gdbGN[gdbGN["VendorID"] == mn])
print("Minimum")
mm = gdbGM["VendorID"].min()
my = gdbGJ["VendorID"].min()
mn = gdbGN["VendorID"].min()
print(gdbGM[gdbGM["VendorID"] == mm])
print(gdbGJ[gdbGJ["VendorID"] == my])
print(gdbGN[gdbGN["VendorID"] == mn])

