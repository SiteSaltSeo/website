from djmoney.models.fields import MoneyField
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db import models
# from Tools.models import Tool


class Plan(models.Model):
    
    name = models.CharField('Plan Title', max_length=40, null=True)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, default=name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("plans", kwargs={"slug":self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Plan.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)

        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_plan_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_plan_receiver, sender=Plan)
