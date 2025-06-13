from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


def credits(request):
    content = "Nicky\nYin Wang"
    return HttpResponse(content, content_type="text/plain")


def about_me(request):
    content = "<html><h4>Hello!</h4>\n<h2>Yin Wang!</h2></html>"
    return HttpResponse(content, content_type="text/html")


def version_info(request):
    content = '{"version": "1.0", "author": "Yin Wang"}'
    return HttpResponse(content, content_type="application/json")


def news(request):
    data = {
        'news': [
            "RiffMates now has a news page!",
            "RiffMates has its first web page.",
        ],
    }
    return render(request, "news.html", data)
