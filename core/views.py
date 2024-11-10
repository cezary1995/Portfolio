from django.shortcuts import render
from django.core.paginator import Paginator
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

from .forms import ContactForm

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
    services = Service.objects.all()
    asked_questions = AskedQuestion.objects.all()
    title = ServicesTitle.objects.first()

    context = {
       'services': services,
       'questions': asked_questions,
       'title': title
    }
    return render(request, 'services.html', context)


def works(request):
    title = WorksTitle.objects.first()
    projects = Project.objects.all()

    paginator = Paginator(projects, 1)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    max_page_links = 3
    start_page = max(page_number - max_page_links // 2, 1)
    end_page = min(start_page + max_page_links - 1, paginator.num_pages)
    page_range = range(start_page, end_page + 1)

    context = {
        'title': title,
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
    max_page_links = 3
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
    title = ContactTitle.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
        message
    context = {
        'title': title,
    }
    return render(request, 'contact.html', context)