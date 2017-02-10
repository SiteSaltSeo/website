from django.contrib import admin
from .models import Articles, Videos, Courses


def make_published(modeladmin, request, queryset):
    queryset.update(published='p')
make_published.short_description = "Mark selected articles as published"

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author', 'published', 'featured',)
    search_field = ['title', 'featured', 'author']
    list_filter = ['published', 'featured', 'author']
    actions = [make_published]

def video_published(modeladmin, request, queryset):
    queryset.update(published='p')
make_published.short_description = "Mark selected videos as published"

class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'author', 'published', 'date_posted' )
    search_field = ['published', 'title', 'featured', 'author']
    list_filter = ['featured','author']
    actions = [video_published]

def course_published(modeladmin, request, queryset):
    queryset.update(published='p')
make_published.short_description = "Mark selected courses as published"

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author', 'published', 'featured',)
    search_field = ['title', 'featured', 'author']
    list_filter = ['published', 'featured','author', 'videos']
    filter_horizontal = ('simillar', 'videos',)
    actions = [course_published]

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(Courses, CoursesAdmin)
