from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/camarita', views.video_page, name='video_page'),
    path('camera_feed/', views.camera_feed, name='camera_feed'),
]
