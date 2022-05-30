from django.contrib import admin
from .models import *
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline


# ordered model admins
class ResourceAdmin(OrderedModelAdmin):
    list_display = ('id', 'link', 'sort_order', 'move_up_down_links')

class TopicTabularInline(OrderedTabularInline):
    model = ResourceToTopic
    fields = ('resource', 'sort_order', 'move_up_down_links',)
    readonly_fields = ('sort_order', 'move_up_down_links',)
    ordering = ('sort_order', )

class TopicAdmin(OrderedModelAdmin):
    list_display = ('topic_name',)
    # exclude = ('resources',)
    inlines = (TopicTabularInline,)

class SkillAdmin(OrderedModelAdmin):
    list_display = ('skill_name', 'move_up_down_links')

# register your models here.
admin.site.register(Superskill)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Resource, ResourceAdmin)