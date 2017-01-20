from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Articles, Videos, Courses
from Pages.models import Page

def learning_centre_overview(request):
    page = Page.objects.filter(page="Learning Center")
    articles = Articles.objects.all()
    videos = Videos.objects.all()
    courses = Courses.objects.all()
    context = {
        "page" : page,
        "articles" : articles,
        "videos" : videos,
        "courses" : courses,
    }

    return render(request, "LearningCentre/page.html", context)

def article_overview(request):

    return render(request, "LearningCentre/articles.html")

def video_overview(request):

    return

def course_overview(request):

    return

def article_detail(request, **kwargs):
    article = get_object_or_404(Articles, slug=kwargs['slug'])
    context = {
        'article': article
    }
    return render(request, "LearningCentre/article-detail.html", context)

def video_detail(request):
    video = get_object_or_404(Videos, slug=kwargs['slug'])
    context = {
        'video': video
    }
    return render(request, "LearningCentre/article-detail.html", context)

def course_detail(request, **kwargs):
    course = get_object_or_404(Courses, slug=kwargs['slug'])
    context = {
        'course': course
    }
    return render(request, "LearningCentre/course-detail.html", context)
