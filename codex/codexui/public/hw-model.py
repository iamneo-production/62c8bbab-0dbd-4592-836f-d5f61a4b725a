# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("heatwave-data.csv")

X = dataset.iloc[:, [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]].values
Y = dataset.iloc[:, -2].values

# Taking Care of Missing data
l = X
for i in range(len(l)):
     for j in range(10):
        if l[i][j] == 'BDL':
            l[i][j] = 'Nan'

for i in range(len(l)):
    for j in range(10):
        if l[i][j] == ' ':
            l[i][j] = 'Nan'

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(X[:, 3:11])
X[:, 3:11] = imputer.transform(X[:, 3:11])
mean = np.nanmean(Y)
Y[np.isnan(Y)] = mean

# Encoding Categorical Data
# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1])], remainder="passthrough")
X = np.array(ct.fit_transform(X))

# Splitting Dataset into Training set and Test set.
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=1)

# Training the Multiple Linear regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the Test set results
Y_test_predicted = regressor.predict(X_test)
np.set_printoptions(precision=2)

# Evaluating the Model Accuracy
from sklearn.metrics import r2_score
r2_score(Y_test, Y_test_predicted)

# Developed By Team Codex
# Credits: Rishit Kumar (Github: CoderX30) , Harsh Anand (Github: anand-harsh)