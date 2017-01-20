from django.contrib import admin
from .models import Articles, Videos, Courses


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'date_posted', 'author',)
    search_field = ['title', 'featured', 'author']
    list_filter = ['featured', 'author']


class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'date_posted', 'author',)
    search_field = ['title', 'featured', 'author']
    list_filter = ['featured','author']

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'date_posted', 'author',)
    search_field = ['title', 'featured', 'author']
    list_filter = ['featured','author', 'videos']
    filter_horizontal = ('simillar', 'videos',)


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(Courses, CoursesAdmin)
