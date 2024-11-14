from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .utils import get_paginator_data
from .models.index import (
    MyExpertArea,WorkExperience, 
    SocialMedia,
)
from .models.about import(
    AboutMe, Review
)
from .models.blog import(
    BlogTitle, BlogArticle
)
from .models.services import(
     ServicesTitle, Service,
     AskedQuestion,
)
from .models.works import(
    WorksTitle, Project
)
from .models.contact import(
    ContactTitle
)

from .forms import UserMessageForm

def index(request):
    expert_area = MyExpertArea.objects.all()
    work_experience = WorkExperience.objects.all()
    social_media = SocialMedia.objects.all()
    services = Service.objects.all()
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
    about_me = AboutMe.objects.first() 
    reviews = Review.objects.all()

    context = {
      'about_me': about_me,
      'reviews': reviews
    }
    return render(request, 'about.html', context)


def services(request):
    title = ServicesTitle.objects.first()
    services = Service.objects.all()
    asked_questions = AskedQuestion.objects.all()
    
    context = {
       'services': services,
       'questions': asked_questions,
       'title': title
    }
    return render(request, 'services.html', context)


def works(request):
    title = WorksTitle.objects.first()
    projects = Project.objects.all()

    # Pagination
    paginator_data = get_paginator_data(request=request, query_set=projects, obj_per_page=1, max_page_links=3)

    context = {
        'title': title,
        'projects': projects,
        'paginator_data': paginator_data
    }
    return render(request, 'works.html', context)


def blog(request):
    title = BlogTitle.objects.first()
    articles = BlogArticle.objects.all()
    
    # Pagination
    paginator_data = get_paginator_data(request=request, query_set=articles, obj_per_page=2, max_page_links=3)

    context = {
        'title': title,
        'articles': articles,
        'paginator_data': paginator_data
    }
    return render(request, 'blog.html', context)


def contact(request):
    title = ContactTitle.objects.first()

    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = UserMessageForm()
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'contact.html', context)