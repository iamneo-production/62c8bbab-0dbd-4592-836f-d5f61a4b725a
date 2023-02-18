from django.shortcuts import render
import joblib
from joblib import load
import sklearn

regressor=load('regressor.joblib')

# Create your views here.
def aqipredictor(request):
    return render(request, 'form.html')

def formInfo(request):

    City=request.GET['City']
    Year=request.GET['Year']
    SO2=request.GET['SO2']
    NH3=request.GET['NH3']
    NOX=request.GET['NOX']
    PM10=request.GET['PM10']
    PM25=request.GET['PM25']
    Y_test_predicted=regressor.predict([[City, Year, SO2, NH3, NOX, PM10, PM25]])
    print(Y_test_predicted)
    return render(request, 'result.html')