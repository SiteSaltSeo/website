from django.db import models
from tinymce.models import HTMLField

class Page(models.Model):

    page = models.CharField("Page:", max_length=200)
    title = models.CharField("Page Title", max_length=200)
    image = models.ImageField("Page Featured Image", blank=True, null=True)
    youtube_id = models.CharField("Youtube Video id", max_length=100, blank=True, null=True)
    keywords = models.TextField("Keywords - meta description", null=True, blank=True)
    structured_data = HTMLField("Structured Data", null=True, blank=True)
    content = models.TextField("Page Content")

    def __str__(self):
        return self.page

