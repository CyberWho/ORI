#%% import

import pandas as pd
import numpy as np
import sklearn
import seaborn as sbrn
import matplotlib.pyplot as plt

#%% data import 

may2015 = pd.read_csv("yellow_tripdata_2015-05.csv", nrows = 1500000)
may2016 = pd.read_csv("yellow_tripdata_2016-05.csv", nrows = 1500000)
may2017 = pd.read_csv("yellow_tripdata_2017-05.csv", nrows = 1500000)
may2018 = pd.read_csv("yellow_tripdata_2018-05.csv", nrows = 1500000)
may2019 = pd.read_csv("yellow_tripdata_2019-05.csv", nrows = 1500000)
#%%
zones = pd.read_csv("taxi_zoness.csv")

#%% clean 

print(may2016.columns)
#%%

del may2016["VendorID"]
#%%
del may2019['RatecodeID']
del may2019['store_and_fwd_flag']
del may2019['payment_type']
del may2019['extra']
del may2019['mta_tax']
del may2019['tip_amount']
del may2019['tolls_amount']
del may2019['improvement_surcharge']
del may2019['total_amount']
del may2019['trip_distance']
#%%
del may2019["congestion_surcharge"]
#del may2019['congestion_surcharge']
 
#%% zones clean

zones.columns
zones = zones.drop(['order', 'hole', 'piece', 'group', 'OBJECTID', 'Shape_Leng', 'Shape_Area', 'id'], axis=1)
zones = zones.drop('Unnamed: 0', axis=1)

zones = zones.groupby('LocationID').mean('long').reset_index()

#def mergeWithZones(dataSet):
#    dataSet = pd.merge(dataSet, zones, left_on='PULocationID', right_index=True, how='left')
#    dataSet = pd.merge(dataSet, zones, left_on='DOLocationID', right_index=True, how='left', suffixes=['_1', '_2'])
#    return dataSet

#may2017 = mergeWithZones(may2017)

#%% MERGE zones with datasets

may2019 = pd.merge(may2019, zones, left_on='PULocationID', right_index=True, how='left')
may2019 = pd.merge(may2019, zones, left_on='DOLocationID', right_index=True, how='left', suffixes=['_1', '_2'])
#%%
del may2019['LocationID_1'], may2019['LocationID_2'], may2019['PULocationID'], may2019['DOLocationID']
#%%
may2017.columns = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'fare_amount', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']    
may2017 = may2017[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'fare_amount']]

#%% create training data

train = pd.concat([may2015, may2016, may2018, may2019])
train.columns

#%% null values

train.isnull().sum()
train = train.dropna(how='any', axis='rows')

#%% invalid prices

train = train.drop(train[train['fare_amount'] < 0].index, axis=0)

#%% invalid coordinates

train = train.drop(((train[train['dropoff_latitude']<-90])|(train[train['dropoff_latitude']>90])).index, axis=0)
train = train.drop(((train[train['dropoff_longitude']<-180])|(train[train['dropoff_longitude']>180])).index, axis=0)

#%% create absolute difference for long and lat and remove outliers

train['diff_lat'] = ( train['dropoff_latitude'] - train['pickup_latitude']).abs()
train['diff_long'] = (train['dropoff_longitude'] - train['pickup_longitude'] ).abs()
train = train[(train.diff_long < 5.0) & (train.diff_lat < 5.0)]

#%% getting rides with 0 passengers

train['passenger_count'].describe()

nulls = train[train['passenger_count'] == 0]
nulls['passenger_count']

#%% preparing for model

train_X = np.column_stack((train.diff_long, train.diff_lat, np.ones(len(train))))
train_Y = np.array(train['fare_amount'])


#%% executing model

weights, _, _, _ = np.linalg.lstsq(train_X, train_Y, rcond = None) 

#%% create test data

test = may2017.drop(['fare_amount'], axis = 1)


test['diff_lat'] = ( test['dropoff_latitude'] - test['pickup_latitude']).abs()
test['diff_long'] = (test['dropoff_longitude'] - test['pickup_longitude'] ).abs()

test_X = np.column_stack((test.diff_long, test.diff_lat, np.ones(len(test))))
test_Y = np.matmul(test_X, weights).round(decimals = 2)


#%% test

submission = pd.DataFrame()
submission['id'] = test.index
submission['fare_amount'] = test_Y


#%% root mean square error

testFareAmount = may2017['fare_amount']
testFareAmount = testFareAmount.dropna(how='any', axis='rows')

submissionFareAmountWithoutNull = submission['fare_amount'].fillna(0)
RMSE = np.sqrt((testFareAmount - submissionFareAmountWithoutNull).mean())
RMSE 

#%% output to CSV

submission = submission.dropna(how='any', axis='rows')
submission.to_csv('submission.csv', index=False)
#%%
k, n = np.polyfit(submission["id"],submission["fare_amount"], 1)
#%%
x_to_plot = np.linspace(0, 1500000, 100)
#%%
plt.plot(may2017.index,may2017["fare_amount"],'o')
plt.plot(x_to_plot, k*x_to_plot + n,color="red")
#%%Real and predicted montly income
print(may2017["fare_amount"].sum())
print(submission["fare_amount"].sum())
#%%Average fare amount
print(may2017["fare_amount"].mean())
print(submission["fare_amount"].mean())