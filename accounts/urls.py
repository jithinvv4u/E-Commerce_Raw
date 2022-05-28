from django.urls import path
from .views import *

urlpatterns = [
    #url for user registration
    path('signup/',SignUpView,name='signup'),
    #url for login(both super_user and other users)
    path('login/',loginView,name='login'),
    #logout user
    path('logout/',logoutView,name='logout'),
    #load index page default when opening
    path('',index,name='index')
]
