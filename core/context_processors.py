from django.core.cache import cache
from .models.index import PersonalInfo, ProfilePicture

def copy_email(request):
    return {'email': 'cezary.rolka95@gmail.com'}

def context_personal_info(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None

    if personal_info:
        return {'name': personal_info.name,
                'short_desc': personal_info.short_desc}

    return  {'name': 'Cezary Rolka',
            'short_desc': 'Python test automation engineer, Sii best worker'}

def context_photo(request):
    photo = ProfilePicture.objects.filter(display=True).first()
    return { 'photo': photo}


