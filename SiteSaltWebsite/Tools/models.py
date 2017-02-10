from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from pricing.models import Plan

# Create your models here.

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Tool(models.Model):

    title = models.CharField(max_length=40)
    icon = models.FileField(null=True, upload_to=upload_location)
    image = models.ImageField("Tool Featured Image",  blank=True, null=True)
    short_description = HTMLField("Short description(max length 150 charachters)", max_length=150, blank=True, null=True)
    description = HTMLField()
    notes = HTMLField("Additioanl Notes for Tooltip", null=True, blank=True)
    slug = models.SlugField(unique=True, default=title)
    featured = models.BooleanField(default=False)
    plan = models.ManyToManyField(Plan, related_name='tools')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("features:featured", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Tool.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)

        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_tool_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_tool_receiver, sender=Tool)
