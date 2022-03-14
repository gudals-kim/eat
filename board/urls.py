
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewjson/', views.viewjson, name='viewjson'),
    path('boardlist/', views.boardList, name='boardList'),
    path('boardview/<str:pk>/', views.boardview, name='boardview'),
    path('boardinsert/', views.boardInsert, name='boardInsert'), 
    path('boardupdate/<str:pk>/', views.boardUpdate, name='boardUpdate'),  
    path('boarddelete/<str:pk>/', views.boardDelete, name='boardDelete'),  
]
