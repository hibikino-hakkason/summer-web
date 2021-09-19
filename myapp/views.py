from django.shortcuts import render

# Create your views here.
def homework(request):
    return render(request, 'homework.html')

def index(request):
    return render(request, 'index.html') 

def recommend(request):
    return render(request, 'recommend.html') 
    