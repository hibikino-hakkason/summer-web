
from django.views import generic
from myapp.models import Movie, Director, Log


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'movie_list'
    queryset = Movie.objects.all()


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'myapp/detail.html'