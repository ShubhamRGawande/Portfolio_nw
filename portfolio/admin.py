from django.contrib import admin
from .models import Skill, Technology, Project, ContactMessage, LearningResource

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'featured')
    list_filter = ('featured', 'date_created')
    search_fields = ('title', 'description')
    filter_horizontal = ('technologies',)
    date_hierarchy = 'date_created'

@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_added', 'featured')
    list_filter = ('category', 'featured', 'date_added')
    search_fields = ('title', 'description', 'link')
    ordering = ('-date_added',)
    list_editable = ('featured',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
