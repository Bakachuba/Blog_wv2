from django.urls import path

from core import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('about/', views.about, name='about'),
]
