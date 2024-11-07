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
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    max_page_links = 4
    start_page = max(page_number - max_page_links // 2, 1)
    end_page = min(start_page + max_page_links - 1, paginator.num_pages)
    page_range = range(start_page, end_page + 1)

    context = {
        'projects': projects,
        'page_obj': page_obj,
        'current_page': page_obj.number,
        'page_range': page_range
    }
    return render(request, 'works.html', context)


def blog(request):
    title = BlogTitle.objects.first()
    articles = BlogArticle.objects.all()

    # Create pagination - 2 obj per page
    paginator = Paginator(articles, 2)
    # Get page num from GET param. and set 1 as a default
    page_number = int(request.GET.get('page', 1))
    # page_obj is class Page's object returned by method get_page(), contains objects assigned to the page
    page_obj = paginator.get_page(page_number)
    # Set max amount nums per page
    max_page_links = 4
    # Declare range of start & end displayed nums
    start_page = max(page_number - max_page_links // 2, 1)
    end_page = min(start_page + max_page_links - 1, paginator.num_pages)
    page_range = range(start_page, end_page + 1)

    context = {
        'title': title,
        'articles': articles,
        'page_obj': page_obj,
        'current_page': page_obj.number,
        'page_range': page_range,
    }

    return render(request, 'blog.html', context)


def contact(request):
    return render(request, 'contact.html')