import time
from django.conf import settings
from django.contrib import admin
from .models.index import (
    MyExpertArea, 
    WorkExperience, 
    SocialMedia,  
    OfferedService, 
    Project, 
    ProfilePicture,
    PersonalInfo
)
from .models.blog import(
    BlogTitle
)


class ProfilePictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'display')
    list_editable = ('display',)
    readonly_fields = ('uploaded_at',)

    # Wbudowana metoda z klasy ModelAdmin, którą nadpisujemy, bo domyślnie nie robi nic
    # Predefiniuje wartości pól formularza przy tworzeniu nowego obiektu w panelu admina
    def get_changeform_initial_data(self, request):
        return {'title': int(time.time())}


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1 # Ilość pustych formularzy do dodania w panelu admina
    can_delete = True  # Ustawienie can_delete na True, aby umożliwić usuwanie


class PersonalInfoAdmin(admin.ModelAdmin):
    inlines = [SocialMediaInline] #zarządzanie social mediami z poziomu klasy PersonalInfo

    def has_add_permission(self, request):
        # Sprawdź, czy istnieje już obiekt w bazie danych
        count = PersonalInfo.objects.count()
        if count >= 1:  # Jeśli jest co najmniej 1 obiekt, wyłącz możliwość dodawania kolejnego
            return False
        return True

#index
admin.site.register(MyExpertArea)
admin.site.register(WorkExperience)
admin.site.register(OfferedService)
admin.site.register(Project)
admin.site.register(ProfilePicture, ProfilePictureAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)

#blog
admin.site.register(BlogTitle)







