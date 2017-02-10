from django.shortcuts import render
from Pages.models import Page
from Tools.models import Tool
from pricing.models import Plan
from LearningCentre.models import Articles, Videos, Courses
from Testimonials.models import Testimonial

# Create your views here.
def index(request):
    pages = Page.objects.filter(page="Home")
    featured = Tool.objects.filter(featured=True)
    tool_all = Tool.objects.all()
    plan = Plan.objects.all()
    tool_filter = Plan.objects.filter(tools__id=1)
    # featured_articles = Articles.objects.filter(featured=True)
    featured_videos = Videos.objects.filter(featured=True).order_by('-date_posted')[:2]
    featured_courses = Courses.objects.filter(featured=True).order_by('-date_posted')[:2]
    testimonial_all = Testimonial.objects.all()

    context = {
        'pages' : pages,
        'featured' : featured,
        'tool_all' : tool_all,
        'plan' : plan,
        'tool_filter' : tool_filter,
        'videos' : featured_videos,
        'courses' : featured_courses,
        'testimonials' : testimonial_all

    }
    return render(request, 'frontend/home.html', context)
