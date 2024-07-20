# from django.contrib import admin
from django.urls import path
import lettings.views


# handler404 = 'oc_lettings_site.views.my_custom_page_not_found_view'


urlpatterns = [
    path('', lettings.views.index, name='lettings_index'),
    path('<int:letting_id>/', lettings.views.letting, name='letting'),
]
