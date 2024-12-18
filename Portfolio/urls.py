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
    path('ai_applications/', AIApplications.as_view(), name="aiapplications"),
    path('ai_ppts/', AIPPTs.as_view(), name="aippts"),
    path('ai_images/', AIImages.as_view(), name="aiimages"),
    path('ai_videos/', AIVideos.as_view(), name="aivideos"),
    path('ai_chatbots/', AIChatbots.as_view(), name="aichatbots"),
    path('project/', ProjectView.as_view(), name="project"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
