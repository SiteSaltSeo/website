from django.shortcuts import render, get_object_or_404
from .models import Tool
from Pages.models import Page

# Create your views here.

def featured_detail(request, **kwargs):

    queryset = get_object_or_404(Tool, slug=kwargs['slug'])
    context = {
        "title" : "test",
        "object_list" : queryset,
    }

    return render(request, "Tools/detail-tool.html", context)

def feature_overview(request):
    queryset = Tool.objects.all()
    pages = Page.objects.filter(page="Featured Tools")
    context = {
        "pages" : pages,
        "object_list" : queryset,
    }

    return render(request, "Tools/overview.html", context)
    