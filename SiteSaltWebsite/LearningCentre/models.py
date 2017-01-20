from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

class Articles(models.Model):

    title = models.CharField("Article Title", max_length=100, default=None, unique=True)
    date_posted = models.DateField("Posted on date", auto_now=False, auto_now_add=False)
    read_time = models.CharField("Article read time", max_length=10, default=None, unique=False)
    short_description = models.TextField(max_length=140, blank=True, null=True)
    image = models.ImageField("Article Featured Image",  blank=True, null=True)
    content = HTMLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(User, null=True, blank=True)
    slug = models.SlugField(unique=True, default=title)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Articles"

class Videos(models.Model):

    title = models.CharField("Video Title", max_length=100, default=None, unique=True)
    date_posted = models.DateField("Posted on date", auto_now=False, auto_now_add=False)
    play_time = models.CharField("Video play time", max_length=10, default=None, unique=False)
    short_description = models.TextField(max_length=140, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    youtube_id = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField("Video Featured Image",  blank=True, null=True)
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(User, null=True, blank=True)
    slug = models.SlugField(unique=True, default=title)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("videos", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Videos"

class Courses(models.Model):

    title = models.CharField("Course Title", max_length=100, default=None, unique=True)
    date_posted = models.DateField("Posted on date", auto_now=False, auto_now_add=False)
    course_time = models.CharField("Course duration", max_length=10, default=None, unique=True)
    short_description = models.TextField(max_length=140, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField("Course Featured Image",  blank=True, null=True)
    featured = models.BooleanField(default=False)
    videos = models.ManyToManyField(Videos, related_name='video', blank=True)
    simillar = models.ManyToManyField("self", blank=True)
    author = models.ForeignKey(User, null=True, blank=True)
    slug = models.SlugField(unique=True, default=title)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Courses"

def create_article_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    querysest = Articles.objects.filter(slug=slug).order_by("-id")
    exists = querysest.exists()

    if exists:
        new_slug = "%s-%s" %(slug, querysest.first().id)

        return create_article_slug(instance, new_slug=new_slug)
    return slug

def create_videos_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    querysest = Videos.objects.filter(slug=slug).order_by("-id")
    exists = querysest.exists()

    if exists:
        new_slug = "%s-%s" %(slug, querysest.first().id)

        return create_videos_slug(instance, new_slug=new_slug)
    return slug

def create_course_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    querysest = Courses.objects.filter(slug=slug).order_by("-id")
    exists = querysest.exists()

    if exists:
        new_slug = "%s-%s" %(slug, querysest.first().id)

        return create_course_slug(instance, new_slug=new_slug)
    return slug


def pre_articles_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_article_slug(instance)

def pre_save_videos_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_videos_slug(instance)

def pre_save_courses_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_course_slug(instance)


pre_save.connect(pre_articles_receiver, sender=Articles)
pre_save.connect(pre_save_videos_receiver, sender=Videos)
pre_save.connect(pre_save_courses_receiver, sender=Courses)