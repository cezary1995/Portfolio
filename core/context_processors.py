from django.core.cache import cache
from .models.index import PersonalInfo, ProfilePicture
from django.views.decorators.cache import cache_page

def copy_email(request):
    return {'email': 'cezary.rolka95@gmail.com'}


def context_personal_info(request):
    cache_key = 'personal_data'
    data = cache.get(cache_key)

    if not data:
        try:
            personal_info = PersonalInfo.objects.first() 
        except PersonalInfo.DoesNotExist:
            personal_info = None
        
        if personal_info:
            data = {'name': personal_info.name,
                            'short_desc': personal_info.short_desc}
        else:
            data = {'name': 'Cezary Rolka',
                            'short_desc': 'Python test automation engineer, Sii best worker'}
            
        cache.set(cache_key, data, timeout=20)

    return data

def context_photo(request):
    cache_key = 'photo_cache'
    cache_photo = cache.get(cache_key)
    if not cache_photo:
        photo = ProfilePicture.objects.filter(display=True).first()
        cache.set(cache_key, photo, timeout=10)

    return {'photo': cache.get(cache_key)}


