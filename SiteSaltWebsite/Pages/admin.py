from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('page', 'title','keywords',)

admin.site.register(Page, PageAdmin)