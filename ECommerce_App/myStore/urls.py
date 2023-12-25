from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
]