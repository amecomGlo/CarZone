from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html("<img src='{}' width='40' style='border-radius:50%' />".format(obj.photo.url))
    
    thumbnail.short_description = 'Photo'
    list_display = ['id','thumbnail', 'first_name', 'last_name','designation', 'created_date']
    list_display_links = ['id', 'first_name','thumbnail']
    search_fields = ['first_name', 'last_name', 'designation',]
    list_filter = ['designation']
admin.site.register(Team, TeamAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'subject']
    list_display_links = ['id', 'name', 'phone']
    
admin.site.register(Message, MessageAdmin)
