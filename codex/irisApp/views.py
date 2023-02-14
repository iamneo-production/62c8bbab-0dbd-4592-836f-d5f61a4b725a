from django.shortcuts import render

# Create your views here.
def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    sepal_length=request.GET['sepal_length']
    sepal_width=request.GET['sepal_width']
    petal_length=request.GET['petal_length']
    petal_width=request.GET['petal_width']
    return render(request, 'result.html')