from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('confession/<int:pk>', views.confession, name='confession'),
    path('confess', views.confess, name='confess'),
    path('about', views.about, name='about'),
]
