def copy_email(request):
    return {'email': 'cezary.rolka95@gmail.com'}

def context_personal_info(request):
    return {
        'name': 'Cezary Rolka',
        'desc': 'Python web-developer with 3 years of experience, I like cookies'
            }