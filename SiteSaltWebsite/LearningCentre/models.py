from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

class PostManager(models.Manager):

    def all(self, *args, **kwargs):

        return super(PostManager, self).filter(published='p').filter(date_posted__lte=timezone.now()
                                                                    )


class Articles(models.Model):

    tags = TaggableManager()
    title = models.CharField("Article Title", max_length=100, default=None, unique=True)
    published = models.CharField("Article status", max_length=1, choices=STATUS_CHOICES, default='p'
                                )
    featured = models.BooleanField(default=False)
    date_posted = models.DateField("Posted on date", auto_now=False, auto_now_add=False)
    read_time = models.CharField("Article read time", max_length=10, default=None, unique=False)
    short_description = models.TextField(max_length=140, blank=True, null=True)
    image = models.ImageField("Article Featured Image", blank=True, null=True,
                              width_field="width_field", height_field="height_field")
    alt_tag = models.CharField("Add an image alt tage", max_length=100, default=None, null=True)
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = HTMLField(blank=True, null=True)
    author = models.ForeignKey(User, null=True, blank=True)
    slug = models.SlugField(unique=True, default=title)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles", kwargs={"slug": self.slug})
        

    class Meta:
        verbose_name_plural = "Articles"

class Videos(models.Model):

    tags = TaggableManager()
    title = models.CharField("Video Title", max_length=100, default=None, unique=True)
    published = models.CharField("Video status", max_length=1, choices=STATUS_CHOICES, default='p')
    featured = models.BooleanField(default=False)
    date_posted = models.DateField("Posted on date", auto_now=False, auto_now_add=False)
    play_time = models.CharField("Video play time", max_length=10, default=None, unique=False)
    short_description = models.TextField(max_length=140, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    youtube_id = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField("Video Featured Image", blank=True, null=True,
                              width_field="width_field", height_field="height_field")
    alt_tag = models.CharField("Add an image alt tage", max_length=100, default=None, null=True)
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, blank=True)
    slug = models.SlugField(unique=True, default=title)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("videos", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Videos"

class Courses(models.Model):

    tags = TaggableManager()
    title = models.CharField("Course Title", max_length=100, default=None, unique=True)
    published = models.CharField("Course status", max_length=1, choices=STATUS_CHOICES, default='p')
    featured = models.BooleanField(default=False)
    date_posted = models.DateField("Posted on date", auto_now=False, auto_now_add=False)
    course_time = models.CharField("Course duration", max_length=10, default=None, unique=True)
    short_description = models.TextField(max_length=140, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField("Course Featured Image", blank=True, null=True,
                              width_field="width_field", height_field="height_field")
    alt_tag = models.CharField("Add an image alt tage", max_length=100, default=None, null=True)
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    videos = models.ManyToManyField(Videos, related_name='video', blank=True)
    simillar = models.ManyToManyField("self", blank=True)
    author = models.ForeignKey(User, null=True, blank=True)
    slug = models.SlugField(unique=True, default=title)

    objects = PostManager()
    
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
