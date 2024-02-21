
from django.urls import path,include
from app.views import *
from django.contrib.auth import logout
from django.conf import settings


urlpatterns = [    
    path('',login),
    path('home',home),
    path('users',view_user),
    path('query_builder', query_builder),
    path('query_output', query_output),
    path('logout', logout_user)
    #path('search', UserViewSet.as_view(), name='search'),
]