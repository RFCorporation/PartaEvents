from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def home_page(request):
    html = template_name="event1.html" 
    return render(request, html)