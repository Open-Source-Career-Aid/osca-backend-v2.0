from django.contrib import admin
from .models import *
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline, OrderedInlineModelAdminMixin

#--------------------------------------------------------------------------------------------------------------------
# XthroughY classes
#--------------------------------------------------------------------------------------------------------------------

# this class defines how the inline for the model 'ResourceThroughTopic' will look like
class ResourceThroughTopicInline(OrderedTabularInline):
    model = ResourceThroughTopic
    list_display = ('resources', 'order',)
    readonly_fields = ('order',)
    ordering = ('order',)
    extra = 0

# this class defines how the inline for the model 'TopicThroughTopic' will look like
# IMPORTANT NOTE: The attribute fk_name was necessary because the model 'TopicThroughTopic' has two foriegn keys to refer to the 'Topic' model
class TopicThroughTopicInline(OrderedTabularInline):
    model = TopicThroughTopic
    fk_name = 'topic'
    list_display = ('subtopics', 'order',)
    readonly_fields = ('order',)
    ordering = ('order',)
    extra = 0

# this class defines how the inline for the model 'TopicThroughSkill' will look like
class TopicThroughSkillInline(OrderedTabularInline):
    model = TopicThroughSkill
    list_display = ('topics', 'order',)
    readonly_fields = ('order',)
    ordering = ('order',)
    extra = 0

# this class defines how the inline for the model 'SkillThroughSuperskill' will look like
class SkillThroughSuperskillInline(OrderedTabularInline):
    model = SkillThroughSuperskill
    list_display = ('skills', 'order',)
    readonly_fields = ('order',)
    ordering = ('order',)
    extra = 0

#--------------------------------------------------------------------------------------------------------------------
# Admin classes
#--------------------------------------------------------------------------------------------------------------------

# Admin for the 'Resource' model
class ResourceAdmin(OrderedModelAdmin):
    list_display = ('link',)

# Admin for the 'Topic' model
class TopicAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Topic
    list_display = ('topicName',)
    inlines = (ResourceThroughTopicInline, TopicThroughTopicInline)

# Admin for the 'Skill' model
class SkillAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Skill
    list_display = ('skillName',)
    inlines = (TopicThroughSkillInline,)

# Admin for the 'Superskill' model
class SuperskillAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Superskill
    list_display = ('superskillName',)
    inlines = (SkillThroughSuperskillInline,)

# admin.site.register for various models
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