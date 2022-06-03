from django.shortcuts import render
from .serializers import *
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getResources(request):
    return JsonResponse(ResourceSerializer(Resource.objects.all(), many=True).data, safe=False)

@api_view(['GET'])
def getTopics(request):
    return JsonResponse(TopicSerializer(Topic.objects.all(), many=True).data, safe=False)

@api_view(['GET'])
def getThrough(request):
    return JsonResponse(ThroughSerializer(ResourceThroughTopic.objects.all(), many=True).data, safe=False)

# ------------
# @api_view(['GET'])
# def getResourcesthroughTopic(request):
#     R = ResourceThroughTopic.objects.all()
#     order_topic_resources = []
#     i = 0
#     for object in R:
#         order_topic_resources[i, 0] = object['order']
#         order_topic_resources[i, 1] = object['topic']
#         order_topic_resources[i, 2] = object['resources']
#         i+=1
#     for j in range(len(i)):
# ------------

#     allResources = ResourceThroughTopic.objects.filter(topic=topicID)
#     resourceIDandOrder = []
#     i = 0
#     for object in allResources:
#         resourceIDandOrder[i, 0] = object.id
#         resourceIDandOrder[i, 0] = object.order


# @api_view(['GET'])
# def getSkills(request):
#     return JsonResponse(SkillSerializer(Skill.objects.all(), many=True).data, safe=False)

# @api_view(['GET'])
# def getSuperskills(request):
#     return JsonResponse(SuperskillSerializer(Superskill.objects.all(), many=True).data, safe=False)