from django.contrib import admin
from .models import Testimonial
# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):

    list_display = ('name', 'company')
    search_fields = ['name', 'company']
    list_filter = ['name', 'company']


admin.site.register(Testimonial, TestimonialAdmin)