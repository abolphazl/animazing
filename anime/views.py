from django.shortcuts import render
from django.views import View
from django.urls import reverse



class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class AnimeDetailsView(View):
    def get(self, request):
        return render(request, 'anime_details.html')