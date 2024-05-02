from django.contrib import admin
from django.urls import path
import lettings.views



urlpatterns = [
    path('', lettings.views.index, name='lettings_index'),
    path('<int:letting_id>/', lettings.views.letting, name='letting'),
]