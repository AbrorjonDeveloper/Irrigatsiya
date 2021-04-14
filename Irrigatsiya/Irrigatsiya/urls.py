
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from teachers.views import TeacherListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("teachers/", TeacherListView.as_view(), name="blog-home"),
    path('teacher/', include('teachers.urls')),
    path('articles/',include("articles.urls")),
    path('books/', include('books.urls')),
    path('events/', include("Events.urls")),
    path('presentations/', include("presentations.urls")),
    path('videos/', include("Videos.urls")),
    path('projects/', include("Projects.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

