from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tool

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
        context = {
            "title" : "test",
            "object_list" : queryset,
        }

        return render(request, "Tools/overview.html", context)