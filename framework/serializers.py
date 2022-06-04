from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.db.models import fields
from .models import *

class ResourceSerializer(serializers.ModelSerializer):

    # order = serializers.SerializerMethodField()

    order = serializers.SerializerMethodField('is_named_bar')

    def is_named_bar(self, Resource):
        through = ResourceThroughTopic.objects.get(resources=Resource.id)
        order = through.order
        return order

    class Meta:
        model = Resource
        fields = ['order', 'link']
    
    # def get_order(self, obj):
    #     Order = ResourceThroughTopic.objects.get(resource=obj.id)
    #     Order = Order.order
    #     return Order

class TopicSerializer(serializers.ModelSerializer):
    relatedResources = ResourceSerializer(many=True)
    class Meta:
        model = Topic
        fields = ['topicName', 'relatedResources']

class ThroughSerializer(serializers.ModelSerializer):

    # topic = serializers.SerializerMethodField()
    # resources = ResourceSerializer()
    # topic = TopicSerializer()

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