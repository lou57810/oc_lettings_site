"""oc_lettings_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import lettings.views
# import profiles.views


# def trigger_error(request):
#     division_by_zero = 1 / 0

# handler404 = 'localhost.views.my_custom_page_not_found_view'


urlpatterns = [
    # path('sentry-debug/', trigger_error),
    path('', lettings.views.home, name='home'),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('admin/', admin.site.urls),
]
