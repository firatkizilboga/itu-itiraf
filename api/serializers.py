#get the user model from django
from . models import User
from django.db import models
#serializer
from rest_framework import serializers

class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'instagram',
            'email',
            'first_name',
            'last_name',
        ]

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'instagram',
            'email',
            'first_name',
            'last_name',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def perform_create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user