from django.urls import path
from . import views
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.index, name='home'),
    # path("register", views.register_request, name="register"),
    # path("login", views.login_request, name="login"),
    # path("logout", views.logout_request, name= "logout"),
    
    
]
