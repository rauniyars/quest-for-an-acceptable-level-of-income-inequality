import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso



# Preparing the data
dataframe = pd.read_csv("Economies.csv")

# Removing all missing, infinite, and NotANumber values (Required to do before any replacement or substitution)
dataframe.replace([np.inf, -np.inf], np.nan, inplace=True)
dataframe.fillna(-99999, inplace=True)

# Check columns whose data types are either integer or float (15 columsn excluding countries)
dataframe.select_dtypes(include=['float','int'])

# Changes datatype of country to numeric (if needed)
dataframe['Country'] = pd.to_numeric(dataframe['Country'], errors='coerce') #Errors='coerce' changes into Nan (Not A Number)
dataframe['Country'].describe()

# if we want to drop ExpEd since it has many missing values (axis = 1 becasue we are dropping column not row)
dataframe.drop(['Country','Year'], inplace=True, axis = 1)


# one hot end coding?
# dataframe = pd.get_dummiesdf_data)
#print(dataframe.describe())

# Separating dependant and independant variables
X = dataframe.drop('GDP per Capita', axis = 1)
y = dataframe['GDP per Capita']

# Splitting into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#print(X_train) #Checking for printing

# Implementing Linear Regression Model
model_linear = LinearRegression()  # Creating a linear object
model_linear.fit(X_train, y_train)                                # Fitting the training data

# Checking the score of the linear model (for training set)
#print(model_linear.score(X_train, y_train)) #0.7151783756588166

# Doing predictions on our test set
y_predict = model_linear.predict(X_test)
# Calculating R-Sqaure on the prediction function (for testing set)
r_square_pre = model_linear.score(X_test, y_test)
print(r_square_pre)
# 0.5844493128603705 # Value dropped from 0.715 to 0.584 and that proves overfitting exists in this data set which is why we cannot use linbear regrssion


# Plotting the linear regression model for actual and predicted data set
plt.plot(y_predict, label = 'predict')
plt.plot(y_test.values, label = 'actual')
plt.ylabel('GDP per Capita')
plt.legend()
plt.show() # Plotted Graph shows major differenec between predicted and actual values


# Section: Printing the coeffecients of the variables
# Grouping all the columns of the training set in X in one variable
feature_col = X_train.columns
# print(feature_col) (Prints all the column names that is 'independant variables')
#Calculating the coeffecients
coef_val = pd.Series(model_linear.coef_, feature_col).sort_values()
print(coef_val)


# Section: Plotting the coeffecients in a bar graph
coef_val.plot(kind='bar', title = 'Plotting the coeffecients of the independant variables')
plt.show()
# The graph shows that the value of coeffecients are higher for Economic Freedom, Openness, GCP
# That means for the overfitting problem that we are having, we need to control the coefficient value of those (above) variables by regularization (through LASSO)
# So now we will implement LASSO and compare the plots


# Section: LASSO REGRESSION
