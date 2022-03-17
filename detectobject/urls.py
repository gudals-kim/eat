from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('detectobject',views.detectobject,name='detectobject'),
    
]