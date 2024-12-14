from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('myworks/', MyWorksView.as_view(), name="myworks"),
    path('project/', ProjectView.as_view(), name="project"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
