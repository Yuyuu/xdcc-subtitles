from django.conf.urls import include, url

urlpatterns = [
    url(r'^subtitles/', include('subtitles.urls')),
]
