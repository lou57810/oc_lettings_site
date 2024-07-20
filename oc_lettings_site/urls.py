from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf.urls import handler404
from django.conf.urls import handler500

import time
from oc_lettings_site.views import index


def homepage_view(request):
    raise Exception("This is a test error")

def trigger_error(request):
    try:
        division_by_zero = 1 / 0

    except Exception as e:
        raise RuntimeError("Critical failure.") from e
        print("Operation forbidden!")
        # return HttpResponse(division_by_zero)
        # handler404 = 'localhost.views.my_custom_page_not_found_view'
        # handler500 = 'localhost.views.my_custom_page_not_found_view'
        # return render(request, 'error500.html')


def large_resource(request):
    time.sleep(4)
    return HttpResponse("Done!")

handler404 = 'oc_lettings_site.views.custom404'
handler500 = 'oc_lettings_site.views.custom500'
urlpatterns = [
    path('', index, name='home'),
    path('sentry-debug/', trigger_error),
    path("home_page_view", homepage_view),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('large_resource/', large_resource),
]
