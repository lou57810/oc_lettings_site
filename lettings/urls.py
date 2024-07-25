# from django.contrib import admin
from django.urls import path
from . import views


# handler404 = 'oc_lettings_site.views.my_custom_page_not_found_view'


urlpatterns = [
    path('index/', views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
