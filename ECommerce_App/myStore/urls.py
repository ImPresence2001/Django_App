from . import views
from django.urls import path

urlpatterns = [
    path('streamlit/', views.streamlit_view, name='streamlit_view'),
    path('login/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
]