#get the user model from django
from . models import User
from django.db import models
#serializer
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
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