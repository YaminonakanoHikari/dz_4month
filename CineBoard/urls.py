from django.urls import path
from .views import *

urlpatterns = [
    path('', FilmListView.as_view(), name='film_list'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('add/', FilmCreateView.as_view(), name='film_add'),
    path('edit/<int:pk>/', FilmUpdateView.as_view(), name='film_edit'),
    path('delete/<int:pk>/', FilmDeleteView.as_view(), name='film_delete'),
]