from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('anime', views.AnimeDetailsView.as_view(), name='anime_page'),
]
