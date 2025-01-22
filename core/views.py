from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django_ratelimit.decorators import ratelimit
from django_ratelimit.core import is_ratelimited
from .utils import get_paginator_data
from .models.index import (
    MyExpertArea,WorkExperience, 
    SocialMedia, SliderText
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

from .forms import UserMessageForm, UserArticleCommentForm

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
    slider = SliderText.objects.filter(view='about').first()


    context = {
      'about_me': about_me,
      'reviews': reviews,
      'trusted': trusted,
      'slider': slider,
    }
    return render(request, 'about.html', context)


def services(request):
    title = ServicesTitle.objects.first()
    services = Service.objects.all()
    asked_questions = AskedQuestion.objects.all()
    slider = SliderText.objects.filter(view='service').first()

    context = {
       'services': services,
       'questions': asked_questions,
       'title': title,
       'slider': slider
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


@ratelimit(key='ip', rate='20/m', method='POST', block=False)
def article(request, slug, article_id):
    article = get_object_or_404(BlogArticle, slug=slug, id=article_id)
    category = article.category
    comments = BlogComment.objects.filter(article=article).order_by('-uploaded_at')

    # Get 2 latest related posts 
    related_posts = BlogArticle.objects.filter(
        category=category).exclude(id=article_id).order_by('-uploaded_at')[:2]
    
    # Check if requests limit has been reached
    if is_ratelimited(request, fn=contact, key='ip', rate='2/m', method='POST', increment=True):
        return JsonResponse(
                {'responseText': 'Too many requests, please wait before post comment again'}, status=429
                )
    
    if request.method == 'POST':
        form = UserArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article', slug=article.slug, article_id=article_id)
    else:
        form = UserArticleCommentForm()
    
    context = {
        'article': article,
        'comments': comments,
        'related_posts': related_posts,
        'form': form,
    }
    return render(request, 'article.html', context)


@csrf_exempt
@ratelimit(key='ip', rate='20/m', method='POST', block=False)
def contact(request):
    title = ContactTitle.objects.first()

    # Check if requests limit has been reached 
    if is_ratelimited(request, fn=contact, key='ip', rate='2/m', method='POST', increment=True):
        return JsonResponse(
                {'responseText': 'Too many requests, wait one minute before send message again.'}, status=429
                )

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
