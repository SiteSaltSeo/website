from django.contrib import admin

# Register your models here.
# from Tools.models import Tool
from .models import Plan

# class ChoiceInline(admin.TabularInline):
#     model = Tool
    



class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    # list_editable = ['price']
    # inlines = [ChoiceInline]

admin.site.register(Plan, PlanAdmin)



