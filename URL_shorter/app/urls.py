from django.urls import path

from . import views

urlpatterns = [
    path('', views.Make, name='Make new'),
    path('!<str:token>', views.UrlInfo, name='Info'),
    path('<str:token>', views.LongUrlPage, name='Long URL Page'),

]