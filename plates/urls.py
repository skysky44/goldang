from django.urls import path

from . import views


app_name = 'plates'
urlpatterns = [
    path('', views.index, name='index'),
]