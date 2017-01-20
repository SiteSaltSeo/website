from __future__ import absolute_import, unicode_literals

from django.db import models
from django import template

register = template.Library()

# class Home_Page(models.Model):
#     page_title = models.CharField(max_length=100, default=None)
#     content = models.TextField()
#     extra_content = models.ForeignKey(content, null=True, blank=True)

#     def __str__(self):
#         return self.page_title 
