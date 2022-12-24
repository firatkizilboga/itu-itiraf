#import the related modules from rest_framework about serializers
from rest_framework import serializers
from .models import Confession, Comment

# Create your serializers here.
class ConfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confession
        fields = [
            'title',
            'body',
            'author',
            'image',
        ]
    
class ConfessionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confession
        fields = [
            'pk',
            'title',
            'body',
            'author',
            'date',
            'likes',
            'comments'
        ]
    
    comments = serializers.SerializerMethodField()
    def get_comments(self, obj):
        return Comment.objects.filter(confession_id = obj.pk).count()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'author',
            'body',
        ]

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'confession_id',
            'author',
            'body',
            'user'
        ]
