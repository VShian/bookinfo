# from django.conf.urls import url
from webpage import views
from django.urls import path

urlpatterns = [
    path('', views.upload, name='upload'),
]