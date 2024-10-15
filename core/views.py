from django.shortcuts import render
from .models.index import (
    MyExpertArea,
    WorkExperience,
    SocialMedia, 
    OfferedService, 
    Project,
)
from .models.blog import(
    BlogTitle
)


def index(request):
    expert_area = MyExpertArea.objects.all()
    work_experience = WorkExperience.objects.all()
    social_media = SocialMedia.objects.all()
    services = OfferedService.objects.all()
    projects = Project.objects.all()

    context = {
       'expert_area': expert_area,
       'work_experience': work_experience,
       'social_media': social_media,
       'services': services,
       'projects': projects,
    }
    
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    services = OfferedService.objects.all()

    context = {
       'services': services,
    }
    return render(request, 'services.html', context)


def works(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'works.html', context)


def blog(request):
    title = BlogTitle.objects.first()

    context = {
        'title': title,
    }

    return render(request, 'blog.html', context)


def contact(request):
    return render(request, 'contact.html')