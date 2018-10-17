from django.contrib import admin
from django.urls import path
from .views import NewsListView


urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
]