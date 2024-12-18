from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, "index.html")

class AboutView(View):
    def get(self, request):
        return render(request, "about.html")

class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")

class MyWorksView(View):
    def get(self, request):
        return render(request, "my_works.html")

class ProjectView(View):
    def get(self, request):
        return render(request, "project.html")

class AIApplications(View):
    def get(self, request):
        return render(request, "extra/ai_applications.html")

class AIPPTs(View):
    def get(self, request):
        return render(request, "extra/ai_ppt.html")

class AIImages(View):
    def get(self, request):
        return render(request, "extra/ai_images.html")

class AIVideos(View):
    def get(self, request):
        return render(request, "extra/ai_video.html")

class AIChatbots(View):
    def get(self, request):
        return render(request, "extra/ai_chatbot.html")
