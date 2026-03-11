from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Changed from 'home' to 'index' to match views.py
    path('browse/', views.browse, name='browse'),
    path('store/<int:restaurant_id>/', views.store_detail, name='store_detail'),
    path('profile/', views.profile, name='profile'),
]