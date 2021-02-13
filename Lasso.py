# Load the Pandas libraries with alias 'pd'
import pandas as pd
from linearmodels import PanelOLS
from linearmodels.panel import PooledOLS
import statsmodels.api as sm
from linearmodels import RandomEffects
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.linear_model import Lasso
from numpy import mean
from numpy import std
from numpy import absolute
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from math import sqrt
from sklearn.metrics import mean_squared_error

# Read data from file 'filename.csv' in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
dataframe = pd.read_csv("Economies.csv")
#print(dataframe.shape)

print(dataframe.describe())

data = dataframe.values
X, y = data[:, :-15], data[:, -1]
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.30,
random_state=20)
print(Xtrain.shape)
print(Xtest.shape)


## Build the lasso model with alpha

model_lasso = Lasso(alpha=10)
model_lasso.fit(Xtrain, ytrain)
pred_train_lasso= model_lasso.predict(Xtrain)
pred_test_lasso= model_lasso.predict(Xtest)

## Evaluate the lasso model
print(np.sqrt(mean_squared_error(ytrain,pred_train_lasso)))
print(r2_score(ytrain, pred_train_lasso))
print(np.sqrt(mean_squared_error(ytest,pred_test_lasso)))
print(r2_score(ytest, pred_test_lasso))
