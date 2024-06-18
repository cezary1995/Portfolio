from django.shortcuts import render
from .models import MyExpertArea, WorkExperience, SocialMediaLink, OfferedService, Project


def index(request):
    expert_area = MyExpertArea.objects.all()
    work_experience = WorkExperience.objects.all()
    social_media_links = SocialMediaLink.objects.all()
    services = OfferedService.objects.all()
    projects = Project.objects.all()

    context = {
       'expert_area': expert_area,
       'work_experience': work_experience,
       'social_media_links': social_media_links,
       'services': services,
       'projects': projects
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def works(request):
    return render(request, 'works.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')