from django.shortcuts import render
from .models.index import (
    MyExpertArea,WorkExperience, 
    SocialMedia, OfferedService, 
    Project,
)
from .models.about import(
    AboutMe, Review

)
from .models.blog import(
    BlogTitle
)
from .models.services import(
    AskedQuestion, ServicesTitle
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
    about_me = AboutMe.objects.all()
    reviews = Review.objects.all()

    context = {
      'about_me': about_me,
      'reviews': reviews
    }
    return render(request, 'about.html', context)


def services(request):
    services = OfferedService.objects.all()
    asked_questions = AskedQuestion.objects.all()
    title = ServicesTitle.objects.first()

    context = {
       'services': services,
       'questions': asked_questions,
       'title': title
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