from django.urls import path
from . import views
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),   
    # path("register", views.register_request, name="register"),
    # path("login", views.login_request, name="login"),
    # path("logout", views.logout_request, name= "logout"),
    
    
]
