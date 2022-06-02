from django.contrib import admin
from .models import *
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline, OrderedInlineModelAdminMixin

class ResourceThroughTopicInline(OrderedTabularInline):
    model = ResourceThroughTopic
    list_display = ('resources', 'order',)
    readonly_fields = ('order',)
    ordering = ('order',)
    extra = 0

class TopicThroughTopicInline(OrderedTabularInline):
    model = TopicThroughTopic
    fk_name = 'topic'
    list_display = ('subtopics', 'order',)
    readonly_fields = ('order',)
    ordering = ('order',)
    extra = 0

class TopicThroughSkillInline(OrderedTabularInline):
    model = TopicThroughSkill
    list_display = ('topics', 'order',)
    readonly_fields = ('order',)
    ordering = ('order',)
    extra = 0

class SkillThroughSuperskillInline(OrderedTabularInline):
    model = SkillThroughSuperskill
    list_display = ('skills', 'order',)
    readonly_fields = ('order',)
    ordering = ('order',)
    extra = 0

class ResourceAdmin(OrderedModelAdmin):
    list_display = ('link',)

class TopicAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Topic
    list_display = ('topicName',)
    inlines = (ResourceThroughTopicInline, TopicThroughTopicInline)

class SkillAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Skill
    list_display = ('skillName',)
    inlines = (TopicThroughSkillInline,)

class SuperskillAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Superskill
    list_display = ('superskillName',)
    inlines = (SkillThroughSuperskillInline,)

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(ResourceThroughTopic)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Superskill, SuperskillAdmin)











# # ordered model admins
# class ResourceAdmin(OrderedModelAdmin):
#     list_display = ('id', 'link', 'sort_order', 'move_up_down_links')

# class TopicTabularInline(OrderedTabularInline):
#     model = ResourceToTopic
#     fields = ('resource', 'sort_order', 'move_up_down_links',)
#     readonly_fields = ('sort_order', 'move_up_down_links',)
#     ordering = ('sort_order', )

# class TopicAdmin(OrderedModelAdmin):
#     list_display = ('topic_name',)
#     # exclude = ('resources',)
#     inlines = (TopicTabularInline,)

# class SkillAdmin(OrderedModelAdmin):
#     list_display = ('skill_name', 'move_up_down_links')

# register your models here.
# admin.site.register(Superskill)
# admin.site.register(Skill)
# admin.site.register(Topic)
# admin.site.register(Resource)