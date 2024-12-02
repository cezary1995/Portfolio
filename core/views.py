from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit
from django.contrib import messages 
from django.utils.timezone import now
from .utils import get_paginator_data
from .models.index import (
    MyExpertArea,WorkExperience, 
    SocialMedia,
)
from .models.about import(
    AboutMe, Review
)
from .models.blog import(
    BlogTitle, BlogArticle,
    BlogComment
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

from .forms import UserMessageForm, UserArticleComment

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
    trusted = len([review for review in reviews if review.rate > 2])

    context = {
      'about_me': about_me,
      'reviews': reviews,
      'trusted': trusted,
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
    paginator_data = get_paginator_data(request=request, query_set=projects, obj_per_page=1)

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
    paginator_data = get_paginator_data(request=request, query_set=articles, obj_per_page=2)

    context = {
        'articles': articles,
        'title': title,
        'articles': articles,
        'paginator_data': paginator_data
    }
    return render(request, 'blog.html', context)


def article(request, slug):

    article = get_object_or_404(BlogArticle, slug=slug)
    comments = BlogComment.objects.all()

    if request.method == 'POST':
        form = UserArticleComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.uploaded_at = now()
            comment.save()
            return redirect('article', slug=article.slug)
    else:
        form = UserArticleComment()
    
    context = {
        'article': article,
        'comments': comments,
        'form': form,
    }

    return render(request, 'article.html', context)


@ratelimit()
def contact(request):
    title = ContactTitle.objects.first()

    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'responseText': 'Message has been sent successfully'})
        return JsonResponse({'responseText': 'Make sure every field is filled in'})
    else:
        form = UserMessageForm()
    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'contact.html', context)
