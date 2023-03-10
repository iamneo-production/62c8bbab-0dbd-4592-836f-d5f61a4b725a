from django.shortcuts import render
from django.http import HttpResponse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from joblib import load
import numpy as np


def aqipredictor(request):
    return render(request, 'form.html')

def predict_aqi(request):
        # Load the regression model
        regressor = load('regressor.joblib')

        # Get the input values from the form
        city=request.GET['city']
        year=float(request.GET['year'])
        month=request.GET['month']
        so2=float(request.GET['so2'])
        nh3=float(request.GET['nh3'])
        nox=float(request.GET['nox'])
        pm10=float(request.GET['pm10'])
        pm25=float(request.GET['pm25'])
        

        # Convert city name to one-hot encoded vector
        city_dict = {'Khammam': [1.0,0.0,0.0,0.0,0.0], 'Adilabad': [0.0,1.0,0.0,0.0,0.0], 'Karimnagar': [0.0,0.0,1.0,0.0,0.0], 'Nizamabad': [0.0,0.0,0.0,1.0,0.0], 'Warangal': [0.0,0.0,0.0,0.0,1.0]}
        city_values = city_dict[city]

        month_dict={'January':[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,0.0 ,0.0, 0.0, 0.0, 0.0], 'Febuary':[0.0, 0.0 ,0.0, 1.0 ,0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0 ,0.0], 'March':[0.0 ,0.0 ,0.0 ,0.0, 0.0 ,0.0 ,0.0, 1.0, 0.0, 0.0 ,0.0, 0.0], 'April':[1.0 ,0.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0], 'May':[0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 'June':[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,0.0, 0.0], 'July':[0.0, 0.0 ,0.0 ,0.0, 0.0 ,1.0 ,0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0], 'August':[0.0 ,1.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0,0.0, 0.0, 0.0 ,0.0 ,0.0], 'September':[0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0 ,0.0, 1.0], 'October':[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'November':[0.0 ,0.0, 0.0, 0.0, 0.0, 0.0,0.0 ,0.0, 0.0, 1.0, 0.0, 0.0], 'December':[0.0, 0.0 ,1.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0 ,0.0]}
        month_values = month_dict[month]

        # Predict AQI index for the input values
        data_point = [city_values + month_values + [year, so2, nh3, nox, pm10, pm25]]
        Y_predicted = regressor.predict(data_point)
        aqi = round(Y_predicted[0], 2)

        # Return the result to the user
        return render(request, 'result.html', {'aqi': aqi, 'city':city, 'year':year, 'month':month, 'so2':so2, 'nh3':nh3, 'nox':nox, 'pm10':pm10, 'pm25':pm25})

# Developed By Team Codex
# Credits: Harsh Anand (Github: anand-harsh), Rishit Kumar 