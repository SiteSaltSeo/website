from django.contrib import admin

# Register your models here.
from pricing.models import Plan
from .models import Tool



class ToolsAdmin(admin.ModelAdmin):

    list_display = ('title', 'icon', "featured")
    search_fields = ['title']
    list_filter = ["featured", "plan"]
    filter_horizontal = ['plan']
    

admin.site.register(Tool, ToolsAdmin)
