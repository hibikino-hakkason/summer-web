from django.shortcuts import redirect, render
from . import create_csv 

# Create your views here.
def homework(request):
    return render(request, 'homework.html')

def index(request):
    return render(request, 'index.html') 

#映画ジャンルを受け取る
def recommend(request):
    result = request.POST.getlist("movie")
    #print(result)
    if request.method == "POST":
        # recommend.py呼びだす
        movies = create_csv.get_movie(result)
            
        return render(request, 'fact.html', { "movies": movies })
    return render(request, 'recommend.html') 

def fact(request):
    return render(request, 'fact.html') 