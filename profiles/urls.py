from django.contrib import admin
from django.urls import path

import profiles.views




urlpatterns = [
    # path('sentry-debug/', trigger_error),
    path('', profiles.views.index, name='profiles_index'),
    path('<str:username>/', profiles.views.profile, name='profile'),
    # path('admin/', admin.site.urls),
]