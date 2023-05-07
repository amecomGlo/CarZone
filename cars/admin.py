from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width=100 style="border-radius:50%">'.format(obj.photo_1.url))
    
    thumbnail.short_description = 'Photo'
    list_display = ('id','thumbnail', 'title','color', 'model', 'year', 'is_featured')
    search_fields = ['title', 'features']
    list_filter =('title', 'model', 'year')
    list_editable = ['is_featured']
    

admin.site.register(Car, CarAdmin)
