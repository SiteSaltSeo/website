from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from Pages.models import Page
from .models import Articles, Videos, Courses


def learning_centre_overview(request):
    pages = Page.objects.filter(page="Learning Center")
    articles_recent = Articles.objects.all()[0:4]
    videos_recent = Videos.objects.all()[0:4]
    courses_recent = Courses.objects.all()[0:4]
    articles_list = Articles.objects.all()
    videos_list = Videos.objects.all()
    courses_list = Courses.objects.all()

    paginator1 = Paginator(articles_list, 3) # Show 25 contacts per page
    paginator2 = Paginator(videos_list, 2)
    paginator3 = Paginator(courses_list, 2)
    page = request.GET.get('page')
    try:
        articles = paginator1.page(page)
        videos = paginator2.page(page)
        courses = paginator3.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator1.page(1)
        videos = paginator2.page(1)
        courses = paginator3.page(1)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator1.page(paginator1.num_pages)
        videos = paginator2.page(paginator2.num_pages)
        courses = paginator3.page(paginator3.num_pages)

    query = request.GET.get("search")
    if query:
        articles = articles_list.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()
        videos = videos_list.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()

        courses = courses_list.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()

    context = {
        "pages" : pages,
        "articles" : articles,
        "videos" : videos,
        "courses" : courses,
        "articles_recent" : articles_recent,
        "videos_recent" : videos_recent,
        "courses_recent" : courses_recent
    }

    return render(request, "LearningCentre/page.html", context)



def article_overview(request):
    pages = Page.objects.filter(page="Articles")
    articles_recent = Articles.objects.all()[0:4]
    articles_list = Articles.objects.all()
    paginator = Paginator(articles_list, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    query = request.GET.get("search")
    if query:
        articles = articles_list.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()

    context = {
        "pages" : pages,
        "articles" : articles,
        "articles_recent" : articles_recent
    }

    return render(request, "LearningCentre/articles.html", context)

def video_overview(request):
    pages = Page.objects.filter(page="Videos")
    videos_list = Videos.objects.all()
    paginator = Paginator(videos_list, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        videos = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        videos = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        videos = paginator.page(paginator.num_pages)

    query = request.GET.get("search")
    if query:
        videos = videos_list.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()

    context = {
        "pages" : pages,
        "videos" : videos,
    }

    return render(request, "LearningCentre/videos.html", context)

def course_overview(request):
    pages = Page.objects.filter(page="Courses")
    courses_list = Courses.objects.all()
    courses_recent = Courses.objects.all()[0:4]
    paginator = Paginator(courses_list, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        courses = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        courses = paginator.page(paginator.num_pages)

    query = request.GET.get("search")
    if query:
        courses = courses_list.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()

    context = {
        "pages" : pages,
        "courses" : courses,
        "courses_recent" : courses_recent,
    }

    return render(request, "LearningCentre/courses.html", context)



def article_detail(request, **kwargs):
    article = get_object_or_404(Articles, slug=kwargs['slug'])
    articles_list = Articles.objects.all().exclude(slug=kwargs['slug'])
    next_article = (Articles.objects.filter(id__gt=article.id).exclude(id=article.id).order_by('id')
                    .first())
    if not article.published == 'p':
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    context = {
        'article': article,
        'articles_list': articles_list,
        'next_article': next_article
    }
    return render(request, "LearningCentre/article-detail.html", context)

def video_detail(request, **kwargs):
    video = get_object_or_404(Videos, slug=kwargs['slug'])
    if video.published == 'd' or video.published == 'w':
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        'video': video
    }
    return render(request, "LearningCentre/video-detail.html", context)

def course_detail(request, **kwargs):
    course = get_object_or_404(Courses, slug=kwargs['slug'])
    course_list = Courses.objects.all().exclude(slug=kwargs['slug'])
    next_course = (Courses.objects.filter(id__gt=course.id).exclude(id=course.id).order_by('id')
                    .first())
    if not course.published == 'p':
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    context = {
        'course': course,
        'course_list': course_list,
        'next_course': next_course
    }
    return render(request, "LearningCentre/course-detail.html", context)
