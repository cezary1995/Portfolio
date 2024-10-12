from .models.index import PersonalInfo, ProfilePicture

def copy_email(request):
    return {'email': 'cezary.rolka95@gmail.com'}

def context_personal_info(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None

    default_data = {'name': 'Cezary Rolka',
                    'short_desc': 'Python test automation engineer, Sii best worker'
                    }
    if personal_info:
        return { 
            'name': personal_info.name,
            'short_desc': personal_info.short_desc
            }
    else:
        return default_data

def context_photo(request):
    photo = ProfilePicture.objects.filter(display=True).first()
    return { 'photo': photo}


