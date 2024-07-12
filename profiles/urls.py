from django.urls import path
import profiles.views


urlpatterns = [
    path('', profiles.views.index, name='profiles_index'),
    path('<str:username>/', profiles.views.profile, name='profile'),
]
