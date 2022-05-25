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
    skill_name = models.CharField(max_length=100)
    # language = models.CharField(max_length=200, blank=True)
    # contributed_by = models.ManyToManyField(User, blank=True)
    # meta_description = models.CharField(max_length=200, blank=True)
    # tags = models.ManyToManyField(Tag, related_name="subskill_tags", blank=True)
    # prerequisites = models.ManyToManyField(Prerequisite, related_name="subskill_prerequisites", blank=True)
    topics = models.ManyToManyField(Topic, related_name="subskill_topics", blank=True)
    # timed_changes = models.DateTimeField(auto_now_add=True)
    # superskills_backlink = models.ForeignKey(Superskill)
    subskills = models.ManyToManyField("self", blank=True, related_name="subskills_under_subskill", symmetrical=False)

    sort_order = models.PositiveIntegerField(editable=False, db_index=True, null=True)
    order_field_name = "sort_order"

    class Meta:
        ordering = ("sort_order",)

    def __str__(self):
        return self.skill_name

class Superskill(models.Model):
    superskill_name = models.CharField(max_length=100)
    # meta_description = models.CharField(max_length=200, blank=True)
    # language = models.CharField(max_length=200, blank=True)
    # contributed_by = models.ManyToManyField(User, blank=True)
    # tags = models.ManyToManyField(
        # Tag, related_name="all_skills_with_this_tag", blank=True)
    # prerequisites = models.ManyToManyField(
        # Prerequisite, related_name="all_skills_with_this_prerequisite", blank=True)
    # sub_superskills = models.ManyToManyField("self", blank=True, related_name="nested_Superskills", symmetrical=False)
    Skills = models.ManyToManyField(Skill, related_name="super_skill", blank=True)
    # timed_changes = models.DateTimeField(auto_now_add=True)

    sort_order = models.PositiveIntegerField(editable=False, db_index=True, null=True)
    order_field_name = "sort_order"

    class Meta:
        ordering = ("sort_order",)

    def __str__(self):
        return self.superskill_name