from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.instagram_feed, name='instagram_feed'),
]
