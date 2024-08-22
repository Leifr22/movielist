from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie,name='home'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/',views.DirectorsList.as_view()),
    path('directors/<int:pk>', views.DirectorsDetail.as_view(),  name='director_list'),
    path('actors/',views.ActorsList.as_view()),
    path('actors/<int:pk>', views.ActorsDeatail.as_view(), name='actors')
]
