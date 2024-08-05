from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.home, name='home'),
    path('base_view/', views.base_view, name='base_view'),
    path('page_profile/', views.page_profile, name='page_profile'),
    path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
]
