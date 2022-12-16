from django.shortcuts import render
#import the api views required to CRUD from rest_framework
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, GenericAPIView
from confession.models import Confession, Comment
from confession.serializers import ConfessionRetrieveSerializer, CommentCreateSerializer,CommentSerializer
#import Response from rest_framework
from rest_framework.response import Response

# Create your views here.

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
    queryset = Confession.objects.all()
    serializer_class = CommentCreateSerializer
    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        body = serializer.validated_data['body']
        if body:
            serializer.save()
        else:
            serializer.save(body=title)


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

    def perform_create(self, serializer):
        serializer.save(confession_id=self.kwargs['pk'])


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

