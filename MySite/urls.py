from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("Polls.urls")),
    path("polls/5", include("Polls.urls")),
    path("polls/5/results", include("Polls.urls")),
    path("polls/5/vote", include("Polls.urls")),
    path('admin/', admin.site.urls),
]
