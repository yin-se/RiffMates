from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def credits(request):
    content = "Nicky\nYin Wang"
    return HttpResponse(content, content_type="text/plain")
