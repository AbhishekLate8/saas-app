from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
# from django.http import h



def home_page_view(request, *args, **kwargs):
    my_title = "my page"
    my_context = {
        "page_title":my_title
    }

    html_template = "home.html"
    print("path",request.path)
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)