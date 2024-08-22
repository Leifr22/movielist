from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Movie,Director,Actor
from django.db.models import F,Max,Min,Count,Avg,Sum,Value
# Create your views here.
def show_all_movie(request):
    movies=Movie.objects.order_by(F('year').desc(nulls_last=True))
    # movies=Movie.objects.annotate(
    #     new_field_bool=Value(True),
    #     new_field_false_bool=Value(False),
    #     new_budget=F('budget')*100,
    #     combined=F('ratings') + F('year')
    #     )
    agg=movies.aggregate(Avg('budget'),Max('year'),Min('ratings'))
    for m in movies:
        m.save()
    return render(request, 'movieapp/all_movies.html',{
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })

def show_one_movie(request, slug_movie: str):
    movie=get_object_or_404(Movie,slug=slug_movie)
    return render(request, 'movieapp/one_movie.html',{
        'movie': movie
    })
# def director_list(request):
#     directors=Director.objects.all()
#     return render(request, 'movieapp/all_directors.html',{
#         'directors': directors
#     })
class DirectorsList(ListView):
    template_name = 'movieapp/all_directors.html'
    model=Director
    context_object_name ='directors'
    paginate_by = 2
# def one_director(request,id_directors: int):
#     director=get_object_or_404(Director,id=id_directors)
#     return render(request,'movieapp/one_director.html',{
#         'director': director
#     })
class DirectorsDetail(DetailView):
    template_name = 'movieapp/one_director.html'
    model=Director
# def actors_list(request):
#     actors=Actor.objects.all()
#     return render(request,'movieapp/all_actors.html',{
#         'actors':actors
#     })
class ActorsList(ListView):
    template_name = 'movieapp/all_actors.html'
    model=Actor
    context_object_name ='actors'
# def one_actor(request,id_actors: int):
#     actor=get_object_or_404(Actor,id=id_actors)
#     return render(request,'movieapp/one_actor.html',{
#         'actor':actor
#     })
class ActorsDeatail(DetailView):
    template_name = 'movieapp/one_actor.html'
    model=Actor