from django.contrib import admin
from .models import *
from ordered_model.admin import OrderedModelAdmin


# ordered model admins
class ResourceAdmin(OrderedModelAdmin):
    list_display = ('link', 'move_up_down_links')

class TopicAdmin(OrderedModelAdmin):
    list_display = ('topic_name', 'move_up_down_links')

class SkillAdmin(OrderedModelAdmin):
    list_display = ('skill_name', 'move_up_down_links')

# register your models here.
admin.site.register(Superskill)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Resource, ResourceAdmin)