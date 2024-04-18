from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='DbD-home'),
    path('about/', views.about, name='DbD-about'),
]
