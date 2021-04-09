import pandas as pd
from sklearn.linear_model import Lasso
from matplotlib import pyplot as plt
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plot
from sklearn.linear_model import Lasso
from numpy import mean
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# Read data from file 'filename.csv' in the same directory that your python process is based)
dataframe = pd.read_csv("Economies.csv")
print(dataframe.shape) # 96 rows, 16 columns
#print(dataframe.describe())

# Removing all missing, infinite, and NotANumber values (Required to do before any replacement or substitution)
dataframe.replace([np.inf, -np.inf], np.nan, inplace=True)
dataframe.fillna(-99999, inplace=True)

#Chooses all rows and columns from 3 to 15 (so all variables)
#dataframe = dataframe.iloc[:,2:15]

# Using pivot tables to summarize the stored data
dataframe = dataframe.pivot_table(values='PPPgw', index='Year',columns='Country')
print(dataframe.head())

# To more easily filter the time series data, later on, we will convert the index into a DateTimeIndex
dataframe.index = pd.to_datetime((dataframe.index),format='%Y').year
print(type(dataframe.index))
print(type(dataframe.columns))
print(dataframe.columns.names)
print(dataframe['US'].head())
print(dataframe.stack().head(10))
print(dataframe.stack(level='Country').head())

# Plotting the dataset
dataframe.mean().sort_values(ascending=False).plot(kind='bar', title="GDP per capita growth in the years 2012 - 2019")

# Set country labels
country_labels = dataframe.mean().sort_values(ascending=False).index.get_level_values('Country').tolist()
plt.xticks(range(0, len(country_labels)), country_labels)
plt.xlabel('Country')
plt.show()

# Passing in axis=1 to .mean() will aggregate over columns (giving the average GPT per capita for all countries over time)
# dataframe.mean(axis=1).head()
# Plotting the above time series data for the average GDP as a line graph (one line)
dataframe.mean(axis=1).plot()
plt.title('Average GDP per capita growth through the years 2012 to 2019')
plt.ylabel('Average GDP per capita growth')
plt.xlabel('Year')
plt.show()

# Line graaph showing all the countries (one line per country)
dataframe.mean(level='Country', axis=1).head()
dataframe.mean(level='Country', axis=1).plot()
plt.title('Average GDP per capita growth through the years 2012 to 2019')
plt.ylabel('Average GDP per capita growth')
plt.xlabel('Year')
plt.show()
dataframe.stack().describe()
