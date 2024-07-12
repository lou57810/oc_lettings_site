# from django.http import HttpResponseNotFound
from sentry_sdk import capture_message
from django.shortcuts import render


def my_custom_page_not_found_view(request, *args, **kwargs):
    capture_message("Page not found!", level="error")
    return render(request, 'error500.html')


def index(request):
    return render(request, 'lettings/home.html')
