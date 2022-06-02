from colorsys import ONE_THIRD
from email.policy import default
from tkinter import CASCADE
from turtle import onclick
from django.db import models
from ordered_model.models import OrderedModel

class Resource(models.Model):
    link = models.TextField(blank=False)
    # relatedTopic = models.ForeignKey('Topic', on_delete=models.CASCADE, null=True)

class Topic(models.Model):
    topicName = models.CharField(max_length=100, blank=False)
    relatedResources = models.ManyToManyField('Resource', through='ResourceThroughTopic', blank=True)
    relatedTopics = models.ManyToManyField('self', through='TopicThroughTopic', blank=True, related_name='relatedTopics')

class ResourceThroughTopic(OrderedModel):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    resources = models.ForeignKey('Resource', on_delete=models.CASCADE)
    order_with_respect_to = 'topic'

    class Meta:
        ordering = ('topic', 'order',)

class TopicThroughTopic(OrderedModel):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='topic')
    subtopics = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='subtopics')
    order_with_respect_to = 'topic'

    class Meta:
        ordering = ('topic', 'order',)

class Skill(models.Model):
    skillName = models.CharField(max_length=100, blank=False)
    relatedTopics = models.ManyToManyField('Topic', through='TopicThroughSkill', blank=True)

class TopicThroughSkill(OrderedModel):
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, related_name='skill')
    topics = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='topics')
    order_with_respect_to = 'skill'

    class Meta:
        ordering = ('skill', 'order',)

class Superskill(models.Model):
    superskillName = models.CharField(max_length=100, blank=False)
    relatedSkills = models.ManyToManyField('Skill', through='SkillThroughSuperskill', blank=True)

class SkillThroughSuperskill(OrderedModel):
    superskill = models.ForeignKey('Superskill', on_delete=models.CASCADE, related_name='superskill')
    skills = models.ForeignKey('Skill', on_delete=models.CASCADE, related_name='skills')
    order_with_respect_to = 'superskill'

    class Meta:
        ordering = ('superskill', 'order',)










# Create your models here.

# class Resource(OrderedModel):

#     topic = models.ForeignKey('Topic', on_delete=models.CASCADE, null=True)
#     class Meta:
#         ordering = ("order",)

#     # resource data feilds
#     link = models.TextField(blank=True)
#     def __str__(self):
#         return self.link

# class Topic(OrderedModel):

#     class Meta:
#         ordering = ("order",)

#     # topic data fields
#     topic_name = models.CharField(max_length=100)
#     # subtopics = models.ManyToManyField("self", blank=True,  related_name="Subtopics", symmetrical=False)
#     # resources = models.ManyToManyField('Resource', blank=True)
#     def __str__(self):
#         return self.topic_name

# # class ResourceToTopic(OrderedModel):

# #     resource = models.ForeignKey('Resource', on_delete=models.CASCADE)
# #     topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
# #     order_with_respect_to = 'topic'

# #     class Meta:
# #         ordering = ('topic', 'order',)

# class Skill(OrderedModel):
  
#     class Meta:
#         ordering = ("order",)

#     # skill data fields
#     skill_name = models.CharField(max_length=100)
#     topics = models.ManyToManyField(Topic, related_name="subskill_topics", blank=True)
#     subskills = models.ManyToManyField("self", blank=True, related_name="subskills_under_subskill", symmetrical=False)
#     def __str__(self):
#         return self.skill_name

# class Superskill(models.Model):
    
#     # superskill data fields
#     superskill_name = models.CharField(max_length=100)
#     Skills = models.ManyToManyField(Skill, related_name="super_skill", blank=True)
#     def __str__(self):
#         return self.superskill_name