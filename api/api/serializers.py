from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ScreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scream
        fields = ['content', 'color', 'expression_points', 'decibel', 'created_at']
    def create(self, validated_data):
        return Scream.objects.create(**validated_data)

class ScreamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scream
        fields = ['content', 'color', 'expression_points', 'decibel', 'created_at']