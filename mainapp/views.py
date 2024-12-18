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


