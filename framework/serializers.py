from rest_framework import serializers
from django.db.models import fields
from .models import *

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        depth = 1

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        depth = 1

class SuperskillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superskill
        fields = '__all__'
        depth = 1