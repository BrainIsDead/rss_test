from django.shortcuts import render
from django.views.generic import ListView
from news.models import News


class NewsListView(ListView):
    template_name = 'home.html'
    model = News
    #queryset = 'news_list'

