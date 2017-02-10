from django.contrib import admin
from .models import Page, Settings
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('page', 'title','keywords',)

admin.site.register(Page, PageAdmin)


admin.site.register(Settings)