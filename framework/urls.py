from django.urls import path
from . import views

urlpatterns = [
    path('get-all-resources/', views.getResources, name='getAllResources'),
    path('get-all-topics/', views.getTopics, name='getAllTopics'),
    path('get-all-skills/', views.getSkills, name='getAllSkills'),
    path('get-all-superskills/', views.getSuperskills, name='getAllSuperskills'),
]