# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:33:40 2023

@author: user
"""

import pandas as pd

# Load dataset
data = pd.read_csv('C:/Users/user/Downloads/GlobalLandTemperatures_GlobalLandTemperaturesByMajorCity.csv')


print(data.head())

# Descriptive statistics
print(data.describe())

import matplotlib.pyplot as plt

data['dt'] = pd.to_datetime(data['dt'])
#graph
# Plot time series
plt.figure(figsize=(10, 6))
plt.plot(data['dt'], data['AverageTemperature'])
plt.title('Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Average Temperature')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data['AverageTemperature'], bins=20)
plt.title('Distribution of Average Temperature')
plt.xlabel('Average Temperature')
plt.ylabel('Frequency')
plt.show()

data['Latitude'] = data['Latitude'].str.replace('N', '').str.replace('S', '').astype(float)

plt.figure(figsize=(8, 6))
plt.scatter(data['Latitude'], data['AverageTemperature'])
plt.title('Latitude vs. Average Temperature')
plt.xlabel('Latitude')
plt.ylabel('Average Temperature')
plt.show()

data['Longitude'] = data['Longitude'].str.replace('W', '').str.replace('E', '').astype(float)

plt.figure(figsize=(8, 6))
plt.scatter(data['Longitude'], data['AverageTemperature'])
plt.title('Longitude vs. Average Temperature')
plt.xlabel('Longitude')
plt.ylabel('Average Temperature')
plt.show()

plt.figure(figsize=(10, 8))
plt.scatter(data['Longitude'], data['Latitude'])
plt.title('Geographical Distribution of Cities')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

country_avg_temp = data.groupby('Country')['AverageTemperature'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
country_avg_temp.plot(kind='bar')
plt.title('Top 10 Countries by Average Temperature')
plt.xlabel('Country')
plt.ylabel('Average Temperature')
plt.xticks(rotation=45)
plt.show()
