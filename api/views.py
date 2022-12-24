from django.shortcuts import render
#import the api views required to CRUD from rest_framework
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, GenericAPIView
#import the api view class
from rest_framework.views import APIView
#import permissions from rest_framework
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from confession.models import Confession, Comment, ConfessionIdentityRelation
from confession.serializers import ConfessionRetrieveSerializer, CommentCreateSerializer,CommentSerializer, ConfessionCreateSerializer
from rest_framework.response import Response
from .serializers import UserRetrieveSerializer, UserCreateSerializer, UserIdentitySerializer
from rest_framework import status

# Create your views here.
from . models import User
class ConfessionLikeView(GenericAPIView):
    queryset = Confession.objects.all()
    serializer_class = ConfessionRetrieveSerializer
    def put(self, request, pk, format=None):
        confession = self.get_object()
        confession.likes += 1
        confession.save()
        serializer = ConfessionRetrieveSerializer(confession)
        return Response(serializer.data)

class ConfessionCreateView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Confession.objects.all()
    serializer_class = ConfessionCreateSerializer
    def post(self,request,format = None):
        serializer = ConfessionCreateSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            serializer.save(user = user, approved = request.user.is_authenticated)
            return Response(serializer.data)
        return Response(serializer.errors)

class ConfessionRetrieveView(RetrieveAPIView):
    queryset = Confession.objects.filter(approved=True)
    serializer_class = ConfessionRetrieveSerializer

class ConfessionListView(ListAPIView):
    queryset = ' '
    def get(self, request, format=None):
        try:
            start = int(request.GET['start'])
            end = int(request.GET['end'])
        except:
            start = 0
            end = 10
        if end-start > 100:
            end = start + 100
        queryset = Confession.objects.filter(approved=True).order_by('-date')[start:end]
        serializer_class = ConfessionRetrieveSerializer(queryset, many=True)
        return Response(serializer_class.data)

class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    authentication_classes = [TokenAuthentication]

    def post(self,request,pk,format = None):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            serializer.save(user = user, confession_id=self.kwargs['pk'])
            return Response(serializer.data)
        return Response(serializer.errors)

class CommentListView(ListAPIView):
    queryset = ' '
    def get(self, request, pk, format=None):
        try:
            start = int(request.GET['start'])
            end = int(request.GET['end'])
        except:
            start = 0
            end = 10
        if end-start > 100:
            end = start + 100
        queryset = Comment.objects.filter(confession_id = pk).order_by('-date')[start:end]
        serializer_class = CommentSerializer(queryset, many=True)
        return Response(serializer_class.data)

class UserRetrieveView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request, format=None):
        user = request.user
        serializer = UserRetrieveSerializer(user)
        return Response(serializer.data)
    
class UserCreateView(APIView):
    def post(self, request):
        permission_classes = [AllowAny]
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#reveal identity
class IdentityRevealView(APIView):
    #accepted methods
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request, pk, format=None):
        user = request.user
        try:
            relation = ConfessionIdentityRelation.objects.create(user=user, confession_id=pk)
            relation.save()
        except Exception:
            return Response(data = ConfessionIdentityRelation.objects.get(confession_id=pk).user.username, status=status.HTTP_200_OK)
        #return create success response
        return Response(status=status.HTTP_201_CREATED)

class UserIdentityListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request, pk, format=None):
        user = request.user
        if Confession.objects.get(pk=pk).user == user:
            queryset = User.objects.filter(confessionidentityrelation__confession_id=pk)
            return Response(UserIdentitySerializer(queryset, many=True).data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)