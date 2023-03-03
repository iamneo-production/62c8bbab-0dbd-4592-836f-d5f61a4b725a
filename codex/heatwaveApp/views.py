from django.shortcuts import render
from django.http import HttpResponse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from joblib import load
import numpy as np


def heatwavepredictor(request):
    return render(request, 'heat-wave.html')

def predict_heatwave(request):
        
        
        # Load the regression model
        regressor = load('model.joblib')

        # Get the input values from the form
        city=request.GET['city']
        year=float(request.GET['year'])
        month=request.GET['month']
        rainfall=float(request.GET['rainfall'])
        mintemp=float(request.GET['mintemp'])
        maxtemp=float(request.GET['maxtemp'])
        minhumidity=float(request.GET['minhumidity'])
        maxhumidity=float(request.GET['maxhumidity'])
        minwindspeed=float(request.GET['minwindspeed'])
        maxwindspeed=float(request.GET['maxwindspeed'])
        
        # Convert city name to one-hot encoded vector
        city_dict = {'Khammam': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 'ADILABAD': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Karimnagar': [0.0, 1.0, 0.0 ,0.0 ,0.0, 0.0], 'Nizamabad': [0.0, 0.0 ,0.0 ,1.0 ,0.0, 0.0], 'WARANGAL R': [0.0 ,0.0 ,0.0, 0.0 ,1.0 ,0.0], 'WARANGAL U': [0.0, 0.0 ,0.0 ,0.0, 0.0, 1.0]}
        city_values = city_dict[city]

        month_dict={'January':[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,0.0 ,0.0, 0.0, 0.0, 0.0], 'Febuary':[0.0, 0.0 ,0.0, 1.0 ,0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0 ,0.0], 'March':[0.0 ,0.0 ,0.0 ,0.0, 0.0 ,0.0 ,0.0, 1.0, 0.0, 0.0 ,0.0, 0.0], 'April':[1.0 ,0.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0], 'May':[0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 'June':[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,0.0, 0.0], 'July':[0.0, 0.0 ,0.0 ,0.0, 0.0 ,1.0 ,0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0], 'August':[0.0 ,1.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0,0.0, 0.0, 0.0 ,0.0 ,0.0], 'September':[0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0 ,0.0, 1.0], 'October':[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'November':[0.0 ,0.0, 0.0, 0.0, 0.0, 0.0,0.0 ,0.0, 0.0, 1.0, 0.0, 0.0], 'December':[0.0, 0.0 ,1.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0 ,0.0]}
        month_values = month_dict[month]

        # Predict AQI index for the input values
        data_point = [city_values + month_values + [year, rainfall, mintemp, maxtemp, minhumidity, maxhumidity, minwindspeed, maxwindspeed]]
        Y_predicted = regressor.predict(data_point)
        heatindex = round(Y_predicted[0], 2)

        # Return the result to the user
        return render(request, 'heatwave-result.html', {'heatindex': heatindex, 'city':city, 'year':year, 'month':month, 'rainfall':rainfall, 'mintemp':mintemp, 'maxtemp':maxtemp, 'maxhumidity':maxhumidity, 'minhumidity':minhumidity, 'minwindspeed':minwindspeed, 'maxwindspeed':maxwindspeed})

# Developed By Team Codex
# Credits: Harsh Anand (Github: anand-harsh), Rishit Kumar