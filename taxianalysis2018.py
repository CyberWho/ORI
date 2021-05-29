# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:21:08 2021

@author: DELL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%Read tabels for may

yellowMay2018 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/yellow_tripdata_2018-05.csv")
greenMay2018 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/green_tripdata_2018-05.csv")

#%%Read tabels for july

yellowJuly2018 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/yellow_tripdata_2018-07.csv")
greenJuly2018 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/green_tripdata_2018-07.csv")

#%%Read tables for november

yellowNovember2018 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/yellow_tripdata_2018-11.csv")
greenNovember2018 = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/green_tripdata_2018-11.csv")

#%%Clean data
yellowMay2018["date"] = yellowMay2018["tpep_pickup_datetime"].str[0:10]
yellowMay2018 = yellowMay2018[("2018-05-01"<=yellowMay2018["date"])&(yellowMay2018["date"]<="2018-05-31")]
greenMay2018["date"] = greenMay2018["lpep_pickup_datetime"].str[0:10]
greenMay2018 = greenMay2018[("2018-05-01"<=greenMay2018["date"])&(greenMay2018["date"]<="2018-05-31")]
yellowJuly2018["date"] = yellowJuly2018["tpep_pickup_datetime"].str[0:10]
yellowJuly2018 = yellowJuly2018[("2018-07-01"<=yellowJuly2018["date"])&(yellowJuly2018["date"]<="2018-07-31")]
greenJuly2018["date"] = greenJuly2018["lpep_pickup_datetime"].str[0:10]
greenJuly2018 = greenJuly2018[("2018-07-01"<=greenJuly2018["date"])&(greenJuly2018["date"]<="2018-07-31")]
yellowNovember2018["date"] = yellowNovember2018["tpep_pickup_datetime"].str[0:10]
yellowNovember2018 = yellowNovember2018[("2018-11-01"<=yellowNovember2018["date"])&(yellowNovember2018["date"]<="2018-11-31")]
greenNovember2018["date"] = greenNovember2018["lpep_pickup_datetime"].str[0:10]
greenNovember2018 = greenNovember2018[("2018-11-01"<=greenNovember2018["date"])&(greenNovember2018["date"]<="2018-11-31")]
#%%Average price for taxi rides 

print(yellowMay2018["total_amount"].mean())
print(greenMay2018["total_amount"].mean())
print(yellowJuly2018["total_amount"].mean())
print(greenJuly2018["total_amount"].mean())
print(yellowNovember2018["total_amount"].mean())
print(greenNovember2018["total_amount"].mean())

#%%Average miles for taxi rides

print(yellowMay2018["trip_distance"].mean())
print(greenMay2018["trip_distance"].mean())
print(yellowJuly2018["trip_distance"].mean())
print(greenJuly2018["trip_distance"].mean())
print(yellowNovember2018["trip_distance"].mean())
print(greenNovember2018["trip_distance"].mean())

#%%Read taxi zones tabel
taxiZones = pd.read_csv("C:/Users/DELL/Desktop/OSNOVI RACUNARSKE INTELIGENCIJE/PROJEKAT/taxi_zones.csv")
#%%Clean taxi zones tabel
del taxiZones["the_geom"]
del taxiZones["Shape_Leng"]
del taxiZones["Shape_Area"]
#%%Merging tabels with taxi zones 

greenMayZones2018 = pd.merge(greenMay2018,taxiZones,left_on="PULocationID",right_index = True,how="left")
greenMayZones2018 = pd.merge(greenMayZones2018,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Merging tabels with taxi zones 

yellowMayZones2018 = pd.merge(yellowMay2018,taxiZones,left_on="PULocationID",right_index=True,how="left")
yellowMayZones2018 = pd.merge(yellowMayZones2018,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Merging tabels with taxi zones 
greenJulyZones2018 = pd.merge(greenJuly2018,taxiZones,left_on="PULocationID",right_index = True,how="left")
greenJulyZones2018 = pd.merge(greenJulyZones2018,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Merging tabels with taxi zones 
yellowJulyZones2018 = pd.merge(yellowJuly2018,taxiZones,left_on="PULocationID",right_index=True,how="left")
yellowJulyZones2018 = pd.merge(yellowJulyZones2018,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Merging tabels with taxi zones 
greenNovemberZones2018 = pd.merge(greenNovember2018,taxiZones,left_on="PULocationID",right_index = True,how="left")
greenNovemberZones2018 = pd.merge(greenNovemberZones2018,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Merging tabels with taxi zones 
yellowNovemberZones2018 = pd.merge(yellowNovember2018,taxiZones,left_on="PULocationID",right_index=True,how="left")
yellowNovemberZones2018 = pd.merge(yellowNovemberZones2018,taxiZones,left_on="DOLocationID",right_index=True,how="left",suffixes=["_1","_2"])
#%%Number of taxi rides grouped by start boroughs in may
gbyYMZ = yellowMayZones2018.groupby("borough_1")["VendorID"].count()
gbyGMZ = greenMayZones2018.groupby("borough_1")["VendorID"].count()
#%%Scatter plot of number of taxi rides in each start borough in may
plt.figure()
plt.plot(gbyYMZ.index, gbyYMZ.values,c="yellow")
plt.plot(gbyGMZ.index,gbyGMZ.values,c="green")
plt.title("Number of taxi rides in each borough in may 2018")
plt.xlabel("Start borough")
plt.ylabel("Number of rides")
#%%Number of taxi rides grouped by start boroughs in july

gbyYYZ = yellowJulyZones2018.groupby("borough_1")["VendorID"].count()
gbyGYZ = greenJulyZones2018.groupby("borough_1")["VendorID"].count()
#%%Scatter plot of number of taxi rides in each start borough in may
plt.figure()
plt.plot(gbyYYZ.index, gbyYYZ.values,c="yellow")
plt.plot(gbyGYZ.index,gbyGYZ.values,c="green")
plt.title("Number of taxi rides in each borough in july 2019")
plt.xlabel("Start borough")
plt.ylabel("Number of rides")
#%%Number of taxi rides grouped by start boroughs in november

gbyYNZ = yellowNovemberZones2018.groupby("borough_1")["VendorID"].count()
gbyGNZ = greenNovemberZones2018.groupby("borough_1")["VendorID"].count()
#%%Scatter plot of number of taxi rides in each start borough in november
plt.figure()
plt.scatter(gbyYNZ.index, gbyYNZ.values,c="yellow",s=gbyYNZ.values/2000)
plt.scatter(gbyGNZ.index,gbyGNZ.values,c="green",s=gbyGNZ.values/2000)
plt.title("Number of taxi rides in each borough in november 2018")
plt.xlabel("Start borough")
plt.ylabel("Number of rides")
#%%Average trip distance in miles for each start/end borough in may 2019

gbyPYM2019 = yellowMayZones2018.groupby("borough_1")["trip_distance"].mean()
gbyDYM2019 = yellowMayZones2018.groupby("borough_2")["trip_distance"].mean()
gbyPGM2019 = greenMayZones2018.groupby("borough_1")["trip_distance"].mean()
gbyDGM2019 = greenMayZones2018.groupby("borough_2")["trip_distance"].mean()
#%%Average trip distance in miles for each start/end borough in july 2019

gbyPYJ2018 = yellowJulyZones2018.groupby("borough_1")["trip_distance"].mean()
gbyDYJ2018 = yellowJulyZones2018.groupby("borough_2")["trip_distance"].mean()
gbyPGJ2018 = greenJulyZones2018.groupby("borough_1")["trip_distance"].mean()
gbyDGJ2018 = greenJulyZones2018.groupby("borough_2")["trip_distance"].mean()
#%%Average trip distance in miles for each start/end borough in november 2019

gbyPYN2018 = yellowNovemberZones2018.groupby("borough_1")["trip_distance"].mean()
gbyDYN2018 = yellowNovemberZones2018.groupby("borough_2")["trip_distance"].mean()
gbyPGN2018 = greenNovemberZones2018.groupby("borough_1")["trip_distance"].mean()
gbyDGN2018 = greenNovemberZones2018.groupby("borough_2")["trip_distance"].mean()
#%%Longest ride in miles (Yellow taxi may 2018)

lrideYM = yellowMayZones2018[yellowMayZones2018["trip_distance"]<=300]
lrideYM = lrideYM["trip_distance"].max()
longestRideYM = yellowMayZones2018[yellowMayZones2018["trip_distance"] == lrideYM]
#%%Longest ride in miles (Green taxi may 2018)

lrideGM = greenMayZones2018["trip_distance"].max()
longestRideGM = greenMayZones2018[greenMayZones2018["trip_distance"] == lrideGM]
#%%Longest ride in miles (Yellow taxi july 2018)
lrideYJ = yellowJulyZones2018["trip_distance"].max()
longestRideYJ = yellowJulyZones2018[yellowJulyZones2018["trip_distance"] == lrideYJ]
#%%Longest ride in miles (Green taxi july 2018)
lrideGJ = greenJulyZones2018["trip_distance"].max()
longestRideGJ = greenJulyZones2018[greenJulyZones2018["trip_distance"] == lrideGJ]
#%%Longest ride in miles (Yellow taxi november 2018)
lrideYN = yellowNovemberZones2018[yellowNovemberZones2018["trip_distance"]<=300]
lrideYN = lrideYN["trip_distance"].max()
longestRideYN = yellowNovemberZones2018[yellowNovemberZones2018["trip_distance"] == lrideYN]
#%%Longest ride in miles (Green taxi november 2018)
lrideGN = greenNovemberZones2018["trip_distance"].max()
longestRideGN = greenNovemberZones2018[greenNovemberZones2018["trip_distance"] == lrideGN]
#%%Most expensive ride (Yellow taxi may 2018)
erideYM = yellowMayZones2018[yellowMayZones2018["total_amount"]<=900]
erideYM = erideYM["total_amount"].max()
mExpensiveYM = yellowMayZones2018[yellowMayZones2018["total_amount"]==erideYM]
#%%Most expensive ride (Green taxi may 2018)
erideGM = greenMayZones2018["total_amount"].max()
mExpensiveGM = greenMayZones2018[greenMayZones2018["total_amount"]==erideGM]
#%%Most expensive ride (Yellow taxi july 2018)
erideYJ = yellowJulyZones2018[yellowJulyZones2018["total_amount"]<=3000]
erideYJ = erideYJ["total_amount"].max()
mExpensiveYJ = yellowJulyZones2018[yellowJulyZones2018["total_amount"]==erideYJ]
#%%Most expensive ride (Green taxi july 2018)
erideGJ = greenJulyZones2018[greenJulyZones2018["total_amount"]<=2000]
erideGJ = erideGJ["total_amount"].max()
mExpensiveGJ = greenJulyZones2018[greenJulyZones2018["total_amount"]==erideGJ]
#%%Most expensive ride (Yellow taxi november 2018)
erideYN = yellowNovemberZones2018["total_amount"].max()
mExpensiveYN = yellowNovemberZones2018[yellowNovemberZones2018["total_amount"]==erideYN]
#%%Most expensive ride (Green taxi november 2018)

erideGN = greenNovemberZones2018[greenNovemberZones2018["total_amount"]<=400]
erideGN = erideGN["total_amount"].max()
mExpensiveGN = greenNovemberZones2018[greenNovemberZones2018["total_amount"]==erideGN]
#%%Parse hour from start time of each ride
greenMayZones2018["hour"] = greenMayZones2018["lpep_pickup_datetime"].str[11:13].astype("int")
greenJulyZones2018["hour"] = greenJulyZones2018["lpep_pickup_datetime"].str[11:13].astype("int")
greenNovemberZones2018["hour"] = greenNovemberZones2018["lpep_pickup_datetime"].str[11:13].astype("int")
#%%Parse hour from start time of each ride
yellowMayZones2018["hour"] = yellowJulyZones2018["tpep_pickup_datetime"].str[11:13].astype("int")
yellowJulyZones2018["hour"] = yellowJulyZones2018["tpep_pickup_datetime"].str[11:13].astype("int")
yellowNovemberZones2018["hour"] = yellowNovemberZones2018["tpep_pickup_datetime"].str[11:13].astype("int")

#%%Histogram for each hour (Green taxi may 2018)
plt.figure()
plt.hist(greenMayZones2018["hour"],bins=20,color="green",edgecolor="blue")
plt.title("Number of taxi rides in each hour in may 2018")
plt.xlabel("Hour")
plt.ylabel("Number of rides")
#%%Histogram for each hour (Yellow taxi may 2018)
plt.figure()
plt.hist(yellowMayZones2018["hour"],bins=20,color="yellow",edgecolor="orange")
plt.title("Number of taxi rides in each hour in may 2018")
plt.xlabel("Hour")
plt.ylabel("Number of rides")
#%%Histogram for each hour (Green taxi july 2018)
plt.figure()
plt.hist(greenJulyZones2018["hour"],bins=20,color="green",edgecolor="blue")
plt.title("Number of taxi rides in each hour in july 2018")
plt.xlabel("Hour")
plt.ylabel("Number of rides")
#%%Histogram for each hour (Yellow taxi july 2018)
plt.figure()
plt.hist(yellowJulyZones2018["hour"],bins=20,color="yellow",edgecolor="orange")
plt.title("Number of taxi rides in each hour in july 2018")
plt.xlabel("Hour")
plt.ylabel("Number of rides")
#%%Histogram for each hour (Green taxi november 2018)
plt.figure()
plt.hist(greenNovemberZones2018["hour"],bins=20,color="green",edgecolor="blue")
plt.title("Number of taxi rides in each hour in november 2018")
plt.xlabel("Hour")
plt.ylabel("Number of rides")
#%%Histogram for each hour (Yellow taxi november 2018)
plt.figure()
plt.hist(yellowNovemberZones2018["hour"],bins=20,color="yellow",edgecolor="orange")
plt.title("Number of taxi rides in each hour in november 2018")
plt.xlabel("Hour")
plt.ylabel("Number of rides")
#%%plot

gbhj = yellowJulyZones2018.groupby("hour")["VendorID"].count()
gbhm = yellowMayZones2018.groupby("hour")["VendorID"].count()
gbhn = yellowNovemberZones2018.groupby("hour")["VendorID"].count()
plt.figure()
plt.plot(gbhm.index,gbhm.values,label="May",color="green")
plt.plot(gbhj.index,gbhj.values,label="July",color="red")
plt.plot(gbhn.index,gbhn.values,label="November",color="blue")
plt.legend(loc="best")
plt.xlabel("Hour")
plt.ylabel("Number of rides")
plt.title("Number of rides for each hour Yellow taxi 2018")
#%%plot

gbhj = greenJulyZones2018.groupby("hour")["VendorID"].count()
gbhm = greenMayZones2018.groupby("hour")["VendorID"].count()
gbhn = greenNovemberZones2018.groupby("hour")["VendorID"].count()
plt.figure()
plt.plot(gbhm.index,gbhm.values,label="May",color="green")
plt.plot(gbhj.index,gbhj.values,label="July",color="red")
plt.plot(gbhn.index,gbhn.values,label="November",color="blue")
plt.legend(loc="best")
plt.xlabel("Hour")
plt.ylabel("Number of rider")
plt.title("Number of rides for each hour Green taxi 2018")
#%%Total number of passengers in each month
print(greenMayZones2018["passenger_count"].sum())
print(greenJulyZones2018["passenger_count"].sum())
print(greenNovemberZones2018["passenger_count"].sum())
print(yellowMayZones2018["passenger_count"].sum())
print(yellowJulyZones2018["passenger_count"].sum())
print(yellowNovemberZones2018["passenger_count"].sum())
#%%Cleaning trip distance for better analysis
ngMay = greenMayZones2018[greenMayZones2018["trip_distance"]<=10]
ngJuly = greenJulyZones2018[greenJulyZones2018["trip_distance"]<=10]
ngNovember = greenNovemberZones2018[(greenNovemberZones2018["trip_distance"]<=10)&(greenNovemberZones2018["trip_distance"]>=0)]
njMay = yellowMayZones2018[yellowMayZones2018["trip_distance"]<=10]
njJuly = yellowJulyZones2018[yellowJulyZones2018["trip_distance"]<=10]
njNovember = yellowNovemberZones2018[yellowNovemberZones2018["trip_distance"]<=10]
#%%More cleaning
ngNovember = greenNovemberZones2018[(greenNovemberZones2018["trip_distance"]<=10)&(greenNovemberZones2018["trip_distance"]>=0)]
njNovember = yellowNovemberZones2018[(yellowNovemberZones2018["trip_distance"]<=10)&(yellowNovemberZones2018["trip_distance"]>=0)]

#%%Histogram for each mile(Green taxi may 2018)
plt.figure()
plt.hist(ngMay["trip_distance"],bins=20,color="green",edgecolor="blue")
plt.xlabel("Trip distance")
plt.ylabel("Number of rides")
plt.title("Number of rides for each mile green taxi may 2018")
#%%Histogram for each mile(Yellow taxi may 2018)
plt.figure()
plt.hist(njMay["trip_distance"],bins=20,color="yellow",edgecolor="orange")
plt.xlabel("Trip distance")
plt.ylabel("Number of rides")
plt.title("Number of rides for each mile yellow taxi may 2018")
#%%Histogram for each mile(Green taxi july 2018)
plt.figure()
plt.hist(ngJuly["trip_distance"],bins=20,color="green",edgecolor="blue")
plt.xlabel("Trip distance")
plt.ylabel("Number of rides")
plt.title("Number of rides for each mile green taxi july 2018")
#%%Histogram for each mile(Yellow taxi july 2018)
plt.figure()
plt.hist(njJuly["trip_distance"],bins=20,color="yellow",edgecolor="orange")
plt.xlabel("Trip distance")
plt.ylabel("Number of rides")
plt.title("Number of rides for each mile yellow taxi july 2018")
#%%Histogram for each mile(Green taxi november 2018)
plt.figure()
plt.hist(ngNovember["trip_distance"],bins=20,color="green",edgecolor="blue")
plt.xlabel("Trip distance")
plt.ylabel("Number of rides")
plt.title("Number of rides for each mile green taxi november 2018")
#%%Histogram for each mile(Yellow taxi november 2018)
plt.figure()
plt.hist(njNovember["trip_distance"],bins=20,color="yellow",edgecolor="orange")
plt.xlabel("Trip distance")
plt.ylabel("Number of rides")
plt.title("Number of rides for each mile yellow taxi november 2018")
#%%Green taxi cash and card paid rides
cashGreenMay = greenMayZones2018[greenMayZones2018["payment_type"] == 2]
cardGreenMay = greenMayZones2018[greenMayZones2018["payment_type"] == 1]
cashGreenJuly = greenJulyZones2018[greenJulyZones2018["payment_type"] == 2]
cardGreenJuly = greenJulyZones2018[greenJulyZones2018["payment_type"] == 1]
cashGreenNovember = greenNovemberZones2018[greenNovemberZones2018["payment_type"] == 2]
cardGreenNovember = greenNovemberZones2018[greenNovemberZones2018["payment_type"] == 1]
#%%Precentage of rides paid by cash and card
print(cashGreenMay["VendorID"].count()/greenMayZones2018["VendorID"].count())
print(cardGreenMay["VendorID"].count()/greenMayZones2018["VendorID"].count())
print(cashGreenJuly["VendorID"].count()/greenJulyZones2018["VendorID"].count())
print(cardGreenJuly["VendorID"].count()/greenJulyZones2018["VendorID"].count())
print(cashGreenNovember["VendorID"].count()/greenNovemberZones2018["VendorID"].count())
print(cardGreenNovember["VendorID"].count()/greenNovemberZones2018["VendorID"].count())
#%%Yellow taxi cash and card paid rides
cashYellowMay = yellowMayZones2018[yellowMayZones2018["payment_type"] == 2]
cardYellowMay = yellowMayZones2018[yellowMayZones2018["payment_type"] == 1]
cashYellowJuly = yellowJulyZones2018[yellowJulyZones2018["payment_type"] == 2]
cardYellowJuly = yellowJulyZones2018[yellowJulyZones2018["payment_type"] == 1]
cashYellowNovember = yellowNovemberZones2018[yellowNovemberZones2018["payment_type"] == 2]
cardYellowNovember = yellowNovemberZones2018[yellowNovemberZones2018["payment_type"] == 1]
#%%Precentage of rides paid by cash and card
print(cashYellowMay["VendorID"].count()/yellowMayZones2018["VendorID"].count())
print(cardYellowMay["VendorID"].count()/yellowMayZones2018["VendorID"].count())
print(cashYellowJuly["VendorID"].count()/yellowJulyZones2018["VendorID"].count())
print(cardYellowJuly["VendorID"].count()/yellowJulyZones2018["VendorID"].count())
print(cashYellowNovember["VendorID"].count()/yellowNovemberZones2018["VendorID"].count())
print(cardYellowNovember["VendorID"].count()/yellowNovemberZones2018["VendorID"].count())
#%%Average tip amount
print(greenMayZones2018["tip_amount"].mean())
print(greenJulyZones2018["tip_amount"].mean())
print(greenNovemberZones2018["tip_amount"].mean())
print(yellowMayZones2018["tip_amount"].mean())
print(yellowJulyZones2018["tip_amount"].mean())
print(yellowNovemberZones2018["tip_amount"].mean())

#%%Average tip amount for card paid rides
print(cardGreenMay["tip_amount"].mean())
print(cardGreenJuly["tip_amount"].mean())
print(cardGreenNovember["tip_amount"].mean())
print(cardYellowMay["tip_amount"].mean())
print(cardYellowJuly["tip_amount"].mean())
print(cardYellowNovember["tip_amount"].mean())

#%%Total montly earning
print(yellowMay2018["total_amount"].sum())
print(greenMay2018["total_amount"].sum())
print(yellowJuly2018["total_amount"].sum())
print(greenJuly2018["total_amount"].sum())
print(yellowNovember2018["total_amount"].sum())
print(greenNovember2018["total_amount"].sum())
#%%Daily earnings (Yellow taxi may 2019)
gym = yellowMayZones2018.groupby("date")["total_amount"].sum()
#%%Plot of daily earnings
plt.figure()
plt.plot(np.arange(1,32),gym.values,color="yellow")
plt.xlabel("Day")
plt.ylabel("Earning")
plt.title("Daily earnings Yellow taxi may 2018")
#%%Plot of daily earnings for Yellow and Green taxi in may 2019
ggm = greenMayZones2018.groupby("date")["total_amount"].sum()
plt.figure()
plt.plot(np.arange(1,32),gym.values,color="yellow",label="Zuti taksi")
plt.plot(np.arange(1,32),ggm.values,color="green",label="Zeleni taksi")
plt.legend(loc="best")
plt.xlabel("Day")
plt.ylabel("Earning")
plt.title("Daily earnings may 2018")

#%%Daily earnings (Yellow taxi july 2019)
gyj = yellowJulyZones2018.groupby("date")["total_amount"].sum()
plt.figure()
plt.plot(np.arange(1,32),gyj.values,color="yellow")
plt.xlabel("Day")
plt.ylabel("Earning")
plt.title("Daily earnings Yellow taxi july 2018")
#%%Daily earning Yellow taxi
plt.figure()
plt.plot(np.arange(1,32),gym.values,color="green",label="May")
plt.plot(np.arange(1,32),gyj.values,color="red",label="July")
plt.plot(np.arange(1,31),gyn.values,color="blue",label="November")
plt.xlabel("Day in month")
plt.ylabel("Earning")
plt.title("Daily earnings Yellow taxi 2018")
plt.legend(loc="best")
#%%Green taxi
ggm = greenMayZones2018.groupby("date")["total_amount"].sum()
ggj = greenJulyZones2018.groupby("date")["total_amount"].sum()
ggn = greenNovember2018.groupby("date")["total_amount"].sum()
#%%Daily earning Green taxi
plt.figure()
plt.plot(np.arange(1,32),ggm.values,color="green",label="May")
plt.plot(np.arange(1,32),ggj.values,color="red",label="July")
plt.plot(np.arange(1,31),ggn.values,color="blue",label="November")
plt.xlabel("Day in month")
plt.ylabel("Earning")
plt.title("Daily earnings Green taxi 2018")
plt.legend(loc="best")

#%%Daily earnings (Yellow taxi july 2018)
gyn = yellowNovemberZones2018.groupby("date")["total_amount"].sum()
plt.figure()
plt.plot(np.arange(1,31),gyn.values,color="yellow")
plt.xlabel("Day")
plt.ylabel("Earning")
plt.title("Daily earnings Yellow taxi november 2018")
#%%Group rides by zones and dates may 2018
gbyZDGM = greenMayZones2018.groupby(["borough_1","date"])["VendorID"].count().reset_index()
gbyZDYM = yellowMayZones2018.groupby(["borough_1","date"])["VendorID"].count().reset_index()
#%%Bronx ride in may group by date
BronxG = gbyZDGM[gbyZDGM["borough_1"] == "Bronx"]
BronxY = gbyZDYM[gbyZDYM["borough_1"] == "Bronx"]
#%%Plot difference
plt.figure()
plt.plot(np.arange(1,32),BronxG["VendorID"],color="green",label="Green taxi")
plt.plot(np.arange(1,32),BronxY["VendorID"],color="yellow",label="Yellow taxi")
plt.title("Taxi rides from Bronx in may 2018")
plt.xlabel("Day")
plt.ylabel("Number of rides")
#%%Brooklyn ride in may group by date
BrooklynG = gbyZDGM[gbyZDGM["borough_1"] == "Brooklyn"]
BrooklynY = gbyZDYM[gbyZDYM["borough_1"] == "Brooklyn"]
#%%Plot difference
plt.figure()
plt.plot(np.arange(1,32),BrooklynG["VendorID"],color="green",label="Green taxi")
plt.plot(np.arange(1,32),BrooklynY["VendorID"],color="yellow",label="Yellow taxi")
plt.title("Taxi rides from Brooklyn in may 2018")
plt.xlabel("Day")
plt.ylabel("Number of rides")
#%%Manhattan ride in may group by date
ManhattanG = gbyZDGM[gbyZDGM["borough_1"] == "Manhattan"]
ManhattanY = gbyZDYM[gbyZDYM["borough_1"] == "Manhattan"]
#%%Plot difference
plt.figure()
plt.plot(np.arange(1,32),ManhattanG["VendorID"],color="green",label="Green taxi")
plt.plot(np.arange(1,32),ManhattanY["VendorID"],color="yellow",label="Yellow taxi")
plt.title("Taxi rides from Manhattan in may 2018")
plt.xlabel("Day")
plt.ylabel("Number of rides")
#%%Queens ride in may group by date
QueensG = gbyZDGM[gbyZDGM["borough_1"] == "Queens"]
QueensY = gbyZDYM[gbyZDYM["borough_1"] == "Queens"]
#%%Plot difference
plt.figure()
plt.plot(np.arange(1,32),QueensG["VendorID"],color="green",label="Green taxi")
plt.plot(np.arange(1,32),QueensY["VendorID"],color="yellow",label="Yellow taxi")
plt.title("Taxi rides from Queens in may 2018")
plt.xlabel("Day")
plt.ylabel("Number of rides")
#%%Staten Island ride in may group by date
StatenIslandG = gbyZDGM[gbyZDGM["borough_1"] == "Staten Island"]
StatenIslandY = gbyZDYM[gbyZDYM["borough_1"] == "Staten Island"]
#%%Plot for Yellow taxi
plt.figure()
plt.plot(np.arange(1,32),BronxY["VendorID"],color="yellow",label="Bronx")
plt.plot(np.arange(1,32),BrooklynY["VendorID"],color="green",label="Brookly")
plt.plot(np.arange(1,32),ManhattanY["VendorID"],color="red",label="Manhattan")
plt.plot(np.arange(1,32),QueensY["VendorID"],color="blue",label="Queens")
plt.plot(np.arange(1,32),StatenIslandY["VendorID"],color="yellow",label="Staten Island")
plt.legend(loc="best")
plt.xlabel("Day")
plt.ylabel("Number of rides")
plt.title("Number of rides in each borough in May 2018 Yellow taxi")
#%%Plot for Green taxi
plt.figure()
plt.plot(np.arange(1,32),BronxG["VendorID"],color="yellow",label="Bronx")
plt.plot(np.arange(1,32),BrooklynG["VendorID"],color="green",label="Brookly")
plt.plot(np.arange(1,32),ManhattanG["VendorID"],color="red",label="Manhattan")
plt.plot(np.arange(1,32),QueensG["VendorID"],color="blue",label="Queens")
plt.plot(np.arange(1,32),StatenIslandG["VendorID"],color="yellow",label="Staten Island")
plt.legend(loc="best")
plt.xlabel("Day")
plt.ylabel("Number of rides")
plt.title("Number of rides in each borough in May 2018 Green taxi")
#%%Plot difference
plt.figure()
plt.plot(np.arange(1,32),StatenIslandG["VendorID"],color="green",label="Green taxi")
plt.plot(np.arange(1,32),StatenIslandY["VendorID"],color="yellow",label="Yellow taxi")
plt.title("Taxi rides from Staten Island in may 2018")
plt.xlabel("Day")
plt.ylabel("Number of rides")
#%%Find most common start zone for Yellow and Green taxi for may,july,november
gbyZGM = greenMayZones2018.groupby("zone_1")["VendorID"].count().reset_index()
gbyZYM = yellowMayZones2018.groupby("zone_1")["VendorID"].count().reset_index()
gbyZGJ = greenJulyZones2018.groupby("zone_1")["VendorID"].count().reset_index()
gbyZYJ = yellowJulyZones2018.groupby("zone_1")["VendorID"].count().reset_index()
gbyZGN = greenNovemberZones2018.groupby("zone_1")["VendorID"].count().reset_index()
gbyZYN = yellowNovemberZones2018.groupby("zone_1")["VendorID"].count().reset_index()
#%%Print results for maximum
maxRidesZGM = gbyZGM["VendorID"].max()
print(gbyZGM.loc[gbyZGM["VendorID"] == maxRidesZGM])
maxRidesZYM = gbyZYM["VendorID"].max()
print(gbyZYM.loc[gbyZYM["VendorID"] == maxRidesZYM])
maxRidesZGJ = gbyZGJ["VendorID"].max()
print(gbyZGJ.loc[gbyZGJ["VendorID"] == maxRidesZGJ])
maxRidesZYJ = gbyZYJ["VendorID"].max()
print(gbyZYJ.loc[gbyZYJ["VendorID"] == maxRidesZYJ])
maxRidesZGN = gbyZGN["VendorID"].max()
print(gbyZGN.loc[gbyZGN["VendorID"] == maxRidesZGN])
maxRidesZYN = gbyZYN["VendorID"].max()
print(gbyZYN.loc[gbyZYN["VendorID"] == maxRidesZYN])
#%%Find most common end zone for Yellow and Green taxi for may,july,november
gbyEGM = greenMayZones2018.groupby("zone_2")["VendorID"].count().reset_index()
gbyEYM = yellowMayZones2018.groupby("zone_2")["VendorID"].count().reset_index()
gbyEGJ = greenJulyZones2018.groupby("zone_2")["VendorID"].count().reset_index()
gbyEYJ = yellowJulyZones2018.groupby("zone_2")["VendorID"].count().reset_index()
gbyEGN = greenNovemberZones2018.groupby("zone_2")["VendorID"].count().reset_index()
gbyEYN = yellowNovemberZones2018.groupby("zone_2")["VendorID"].count().reset_index()
#%%Print results for maximum
maxRidesEGM = gbyEGM["VendorID"].max()
print(gbyEGM.loc[gbyEGM["VendorID"] == maxRidesEGM])
maxRidesEYM = gbyEYM["VendorID"].max()
print(gbyEYM.loc[gbyEYM["VendorID"] == maxRidesEYM])
maxRidesEGJ = gbyEGJ["VendorID"].max()
print(gbyEGJ.loc[gbyEGJ["VendorID"] == maxRidesEGJ])
maxRidesEYJ = gbyEYJ["VendorID"].max()
print(gbyEYJ.loc[gbyEYJ["VendorID"] == maxRidesEYJ])
maxRidesEGN = gbyEGN["VendorID"].max()
print(gbyEGN.loc[gbyEGN["VendorID"] == maxRidesEGN])
maxRidesEYN = gbyEYN["VendorID"].max()
print(gbyEYN.loc[gbyEYN["VendorID"] == maxRidesEYN])
#%%Print results for maximum
minRidesZGM = gbyZGM["VendorID"].min()
print(gbyZGM.loc[gbyZGM["VendorID"] == minRidesZGM])
minRidesZYM = gbyZYM["VendorID"].min()
print(gbyZYM.loc[gbyZYM["VendorID"] == minRidesZYM])
minRidesZGJ = gbyZGJ["VendorID"].min()
print(gbyZGJ.loc[gbyZGJ["VendorID"] == minRidesZGJ])
minRidesZYJ = gbyZYJ["VendorID"].min()
print(gbyZYJ.loc[gbyZYJ["VendorID"] == minRidesZYJ])
minRidesZGN = gbyZGN["VendorID"].min()
print(gbyZGN.loc[gbyZGN["VendorID"] == minRidesZGN])
minRidesZYN = gbyZYN["VendorID"].min()
print(gbyZYN.loc[gbyZYN["VendorID"] == minRidesZYN])