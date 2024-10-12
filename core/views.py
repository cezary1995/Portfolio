from core.context_processors import context_personal_info
from django.shortcuts import render
from .models.index import (
    MyExpertArea,
    WorkExperience,
    SocialMedia, 
    OfferedService, 
    Project,
    ProfilePicture,
    PersonalInfo
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

    # context_data = context_personal_info(request)
    # default_desc = context_data['desc']

    # Add defalut personal info if it couldn't be get from db or 'desc' field is empty
    # if not personal_info.short_desc:
    #     print
    #     personal_info.short_desc = default_desc
    #     personal_info.save()

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
    return render(request, 'services.html')

def works(request):
    return render(request, 'works.html')

def blog(request):
    title = BlogTitle.objects.first()

    context = {
        'title': title,
    }

    return render(request, 'blog.html', context)

def contact(request):
    return render(request, 'contact.html')