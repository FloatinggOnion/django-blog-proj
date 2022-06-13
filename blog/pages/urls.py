from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('quickreads/', views.quickreads, name='quickreads'),
]