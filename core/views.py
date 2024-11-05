from django.shortcuts import render
from django.core.paginator import Paginator
from .models.index import (
    MyExpertArea,WorkExperience, 
    SocialMedia, OfferedService, 
    Project,
)
from .models.about import(
    AboutMe, Review

)
from .models.blog import(
    BlogTitle, BlogArticle
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
    about_me = AboutMe.objects.first() 
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

    paginator = Paginator(projects, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    current_page = page_obj.number
    pages = range(1, paginator.num_pages + 1)

    max_page_links = 4

    context = {
        'projects': projects,
        'page_obj': page_obj,
        'current_page': current_page,
        'pages': pages
    }
    return render(request, 'works.html', context)


def blog(request):
    title = BlogTitle.objects.first()
    articles = BlogArticle.objects.all()

    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    current_page = page_obj.number
    pages = range(1, paginator.num_pages + 1)

    context = {
        'title': title,
        'articles': articles,
        'page_obj': page_obj,
        'current_page': current_page,
        'pages': pages
    }

    return render(request, 'blog.html', context)


def contact(request):
    return render(request, 'contact.html')