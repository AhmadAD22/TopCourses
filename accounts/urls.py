from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import *
from .views.home import *


urlpatterns = [
    # Signup URL
    path('signup/',signup_view, name='signup'),
    path('login',login_view,name="login"),
    path('logout',logout_view,name="logout"),
    
]
