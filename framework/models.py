from email.policy import default
from django.db import models
from ordered_model.models import OrderedModel

class Resource(models.Model):
    link = models.TextField(blank=True)
    # relatedTopic = models.ForeignKey('Topic', on_delete=models.CASCADE, null=True)

class Topic(OrderedModel):
    topicName = models.CharField(max_length=100, blank=True)
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