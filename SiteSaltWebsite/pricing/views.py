from django.shortcuts import render, get_object_or_404
from .models import Plan
from Tools.models import Tool
from Pages.models import Page

def overall(request):
    plan = Plan.objects.all()
    pages = Page.objects.filter(page="Plans")
    tools = Tool.objects.all()
    
    context = {
        'plan': plan,
        'pages': pages,
        'tools': tools
    }
    template_name = 'pricing/plans-page.html'

    return render(request, template_name, context)



def table(request):
    context= locals()
    template_name = 'pricing/table.html'
    return render(request, template_name, context)

def individual(request, **kwargs):
    plan = get_object_or_404(Plan, slug=kwargs['slug'])
    context = {
        'plan': plan
    }
    template_name = 'pricing/individual-feature.html'
    return render(request, template_name, context)
    