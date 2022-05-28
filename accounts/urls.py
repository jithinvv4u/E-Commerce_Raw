from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',SignUpView,name='signup'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    path('',index,name='index')
]
