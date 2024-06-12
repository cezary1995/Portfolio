from django.shortcuts import render
from .models import My_expert_area, Work_experience


def index(request):
    skills = My_expert_area.objects.all()
    experience = Work_experience.objects.all()

    context = {
       'skills': skills,
       'work_experience': experience
    }
    print(request.path)
    return render(request, 'index.html', context)

def about(request):
    print(request.path)
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def works(request):
    return render(request, 'works.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')