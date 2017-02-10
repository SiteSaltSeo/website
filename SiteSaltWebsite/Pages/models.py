from django.db import models
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField
from django.utils import timezone


class PostManager(models.Manager):
    def all(self, *args, **kwargs):

        return super(PostManager, self).filter(published='p').filter(date_posted__lte=timezone.now()
                                                                    )


class Page(models.Model):

    page = models.CharField("Page:", max_length=200)
    title = models.CharField("Page Title", max_length=200)
    image = models.ImageField("Page Featured Image", blank=True, null=True)
    youtube_id = models.CharField("Youtube Video id", max_length=100, blank=True, null=True)
    keywords = models.TextField("Keywords - meta description", null=True, blank=True)
    structured_data = HTMLField("Structured Data", null=True, blank=True)
    content = models.TextField("Page Content")

    objects = PostManager()
    def __str__(self):
        return self.page


def validate_only_one_instance(obj):

    model = obj.__class__

    if model.objects.count() > 0 and obj.id != model.objects.get().id:
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class Settings(models.Model):

    google_analytics = models.CharField("Google Analytics code", max_length=100, default=None,
                                        null=True, blank=True, unique=True)
    google_handle = models.CharField("Google +", max_length=150, default=None,
                                       blank=True, null=True, unique=True)
    facebook_handle = models.CharField("Facebook handle", max_length=100, default=None,
                                       blank=True, null=True, unique=True)
    youtube_handle = models.CharField("Youtube channel", max_length=300, default=None,
                                       blank=True, null=True, unique=True)
    twitter_handle = models.CharField("Twiiter handle", max_length=100, default=None,
                                      blank=True, null=True, unique=True)

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = "Settings"

    def __str__(self):
        return "SiteSalt Social Settings"
