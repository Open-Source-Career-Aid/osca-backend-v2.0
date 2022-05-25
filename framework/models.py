from email.policy import default
from django.db import models
from ordered_model.models import OrderedModelBase

# Create your models here.
class Resource(OrderedModelBase):

    # order model
    sort_order = models.PositiveIntegerField(editable=False, db_index=True, null=True)
    order_field_name = "sort_order"
    class Meta:
        ordering = ("sort_order",)

    # resource data feilds
    link = models.TextField(blank=True)
    def __str__(self):
        return self.link

class Topic(OrderedModelBase):

    # order model
    sort_order = models.PositiveIntegerField(editable=False, db_index=True, null=True)
    order_field_name = "sort_order"
    class Meta:
        ordering = ("sort_order",)

    # topic data fields
    topic_name = models.CharField(max_length=100)
    subtopics = models.ManyToManyField("self", blank=True,  related_name="Subtopics", symmetrical=False)
    resources = models.ManyToManyField(Resource, blank=True)
    def __str__(self):
        return self.topic_name

class Skill(OrderedModelBase):
  
    # order model
    sort_order = models.PositiveIntegerField(editable=False, db_index=True, null=True)
    order_field_name = "sort_order"
    class Meta:
        ordering = ("sort_order",)

    # skill data fields
    skill_name = models.CharField(max_length=100)
    topics = models.ManyToManyField(Topic, related_name="subskill_topics", blank=True)
    subskills = models.ManyToManyField("self", blank=True, related_name="subskills_under_subskill", symmetrical=False)
    def __str__(self):
        return self.skill_name

class Superskill(models.Model):

    # order model
    sort_order = models.PositiveIntegerField(editable=False, db_index=True, null=True)
    order_field_name = "sort_order"
    class Meta:
        ordering = ("sort_order",)
    
    # superskill data fields
    superskill_name = models.CharField(max_length=100)
    Skills = models.ManyToManyField(Skill, related_name="super_skill", blank=True)
    def __str__(self):
        return self.superskill_name