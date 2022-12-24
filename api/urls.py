#import django path
from django.urls import path
#import obtainauthtoken
from rest_framework.authtoken.views import ObtainAuthToken


from . import views

urlpatterns = [
    path('user/login', ObtainAuthToken.as_view(), name='auth'),
    path('user', views.UserRetrieveView.as_view(), name='user'),
    path('user/create', views.UserCreateView.as_view(), name='user-create'),
    path('confession/<int:pk>', views.ConfessionRetrieveView.as_view(), name='confession'),
    path('confessions', views.ConfessionListView.as_view(), name='confessions'),
    path('confession/create', views.ConfessionCreateView.as_view(), name='confession-create'),
    path('confession/<int:pk>/comment/create', views.CommentCreateView.as_view(), name='confession-comment'),
    path('confession/<int:pk>/comments', views.CommentListView.as_view(), name='confession-comments'),
    path('confession/<int:pk>/like', views.ConfessionLikeView.as_view(), name='confession-like'),
]