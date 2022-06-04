from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.db.models import fields
from .models import *

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['link']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['topicName']

class ThroughSerializer(serializers.ModelSerializer):

    # topic = serializers.SerializerMethodField()
    resources = ResourceSerializer()
    topic = TopicSerializer()

    class Meta:
        model = ResourceThroughTopic
        fields = ['order', 'topic', 'resources']
        depth = 0

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