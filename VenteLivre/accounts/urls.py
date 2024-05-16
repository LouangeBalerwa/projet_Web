from django.urls import path
from . import views

# app_name = "accounts"

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
]
