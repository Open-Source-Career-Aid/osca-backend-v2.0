from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.db.models import fields
from .models import *

class ThroughSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceThroughTopic
        fields = ['order', 'topic', 'resources']
        depth = 0

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'link', 'orderwrttopic']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topicName', 'relatedResources']
        depth = 2

# returning the ordered list for resources according to topic

# ------------

# class ResourceThroughTopicSerializer(serializers.Serializer):
#     topic = 
# ------------

# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = '__all__'
#         depth = 1

# class SuperskillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Superskill
#         fields = '__all__'
#         depth = 1