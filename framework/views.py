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

# @api_view(['GET'])
# def getSkills(request):
#     return JsonResponse(SkillSerializer(Skill.objects.all(), many=True).data, safe=False)

# @api_view(['GET'])
# def getSuperskills(request):
#     return JsonResponse(SuperskillSerializer(Superskill.objects.all(), many=True).data, safe=False)