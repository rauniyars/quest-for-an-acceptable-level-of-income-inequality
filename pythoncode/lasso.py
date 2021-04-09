import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# SECTION: DATA PREPROCESSING

# Preparing the data
dataframe = pd.read_csv("Economies.csv")

# Filtering data for the all the countries (current analysis for US)
dataframe = dataframe[dataframe['Country'] == "US"]
#dataframe = dataframe[dataframe['Country'] == "Germany"]
#dataframe = dataframe[dataframe['Country'] == "Australia"]
#dataframe = dataframe[dataframe['Country'] == "Japan"]
#dataframe = dataframe[dataframe['Country'] == "Israel"]
#dataframe = dataframe[dataframe['Country'] == "China"]
#dataframe = dataframe[dataframe['Country'] == "India"]
#dataframe = dataframe[dataframe['Country'] == "Russia"]
#dataframe = dataframe[dataframe['Country'] == "South Africa"]
#dataframe = dataframe[dataframe['Country'] == "Mexico"]
#dataframe = dataframe[dataframe['Country'] == "Nepal"]
#dataframe = dataframe[dataframe['Country'] == "Nigeria"]

# Removing all missing, infinite, and NotANumber values (Required to do before any replacement or substitution)
dataframe.replace([np.inf, -np.inf], np.nan, inplace=True)
dataframe.fillna(-99999, inplace=True)

# Check columns whose data types are either integer or float (15 columns excluding countries)
dataframe.select_dtypes(include=['float','int'])

# Changes datatype of country to numeric (if needed)
dataframe['Country'] = pd.to_numeric(dataframe['Country'], errors='coerce') #Errors='coerce' changes into Nan (Not A Number)
dataframe['Country'].describe()

# Dropping country and year column data
dataframe.drop(['Country','Year'], inplace=True, axis = 1)
print(dataframe.head())

# dataframe = pd.get_dummiesdf_data)
#print(dataframe.describe())

# Separating dependent and independent variables
X = dataframe.drop('PPPgw', axis = 1) #Dropping GDP as we are predicting it
y = dataframe['PPPgw']

# Splitting into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
#print(X_train) #Checking for printing


# SECTION: IMPLEMENTING THE LASSO MODEL

# Creating an object for LASSO
model_lasso = Lasso(alpha=0.000007, normalize=True)    #normalize=True helps with standardization of the data, if some value is a higher value, then the weight of the value wont be counted as a lot
# Fitting our training data in the model
model_lasso.fit(X_train, y_train)
# Checking the score for lasso regression
#print(model_lasso.score(X_train, y_train))
lasso_coef = model_lasso.fit(X,y).coef_

names = dataframe.drop('PPPgw',axis=1).columns

plt.plot(range(len(names)),lasso_coef)
plt.xticks(range(len(names)),names,rotation=60)
plt.ylabel("coefficients")
plt.show()

# Doing predictions on the test set
y_predict = model_lasso.predict(X_test)
# Calculating R-Square on the prediction function (for testing set)
r_square_lasso = model_lasso.score(X_test, y_test)

#print(r_square_lasso)
print('Lasso Regression: R^2 score on training set', model_lasso.score(X_train, y_train)*100)
print('Lasso Regression: R^2 score on test set', model_lasso.score(X_test, y_test)*100)

# Plotting the linear regression model for actual and predicted data set
plt.plot(y_predict, label = 'predict')
plt.plot(y_test.values, label = 'actual')
plt.ylabel('PPP')
plt.legend()
plt.show()

# Section: Printing the coeffecients of the variables
# Grouping all the columns of the training set in X in one variable
feature_col = X_train.columns
#print(feature_col) (Prints all the column names that is 'independant variables')
#Calculating the coeffecients
coef_val = pd.Series(model_lasso.coef_, feature_col).sort_values()
#print(coef_val)

# Section: Plotting the coeffecients in a bar graph
coef_val.plot(kind='bar', title = 'Plotting the coeffecients of the independant variables')
plt.show()
