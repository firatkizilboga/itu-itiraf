#import django path
from django.urls import path
from . import views

urlpatterns = [
    path('confession/<int:pk>', views.ConfessionRetrieveView.as_view(), name='confession'),
    path('', views.ConfessionListView.as_view(), name='home'),
    path('confession/create', views.ConfessionCreateView.as_view(), name='confession-create'),
    path('confession/<int:pk>/comment/create', views.CommentCreateView.as_view(), name='confession-comment'),
    path('confession/<int:pk>/comments', views.CommentListView.as_view(), name='confession-comments'),
    path('confession/<int:pk>/like', views.ConfessionLikeView.as_view(), name='confession-like'),
]
