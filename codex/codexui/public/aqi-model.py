# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv("aqi-data.csv")
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , -1].values


# Taking Care of Missing data

l = X
for i in range(len(l)):
    for j in range(8):
        if l[i][j] == 'BDL':
            l[i][j] = 'Nan'

for i in range(len(l)):
    for j in range(8):
        if l[i][j] == ' ':
            l[i][j] = 'Nan'


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer.fit(X[:, 2:10])
X[:,2:10] = imputer.transform(X[:,2:10])

mean = np.nanmean(Y)
Y[np.isnan(Y)] = mean

# Encoding Categorical Data

## Encoding the Independent Variable

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder() , [0,1])], remainder="passthrough")
X = np.array(ct.fit_transform(X))

# Splitting Dataset into Training set and Test set.

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=1)

# Training the Lasso regression model on the Training set

from sklearn.linear_model import Lasso
regressor = Lasso()
regressor.fit(X_train, Y_train)

# Predicting the result of the test set

Y_predicted = regressor.predict(X_test)
np.set_printoptions(precision =2)

# Evaluating the Model Accuracy

from sklearn.metrics import r2_score
r2_score(Y_test, Y_predicted)

# Developed By Team Codex
# Credits:  Rishit Kumar(Github: CoderX30), Harsh Anand (Github: anand-harsh)