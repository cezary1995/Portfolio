from django.core.cache import cache
from .models.index import PersonalInfo, ProfilePicture

from django.utils.translation import gettext as _
from django.utils.translation import get_language

def copy_email(request):
    return {'email': 'cezary.rolka95@gmail.com'}


def context_personal_info(request):
    lang = get_language()

    try:
        personal_info = PersonalInfo.objects.first()
        description = personal_info.short_desc
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    if personal_info:
        data = {
            'name': personal_info.name,
            'short_desc': description
            }
    else:
        data = {
            'name': 'Cezary Rolka',
            'short_desc': description
            }    
    return data


def context_photo(request):
    cache_key = 'photo_cache'
    cache_photo = cache.get(cache_key)
    if not cache_photo:
        photo = ProfilePicture.objects.filter(display=True).first()
        cache.set(cache_key, photo, timeout=10)

    return {'photo': cache.get(cache_key)}


