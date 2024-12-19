import time
from django.contrib import admin
from .models.index import (
    MyExpertArea, WorkExperience, 
    SocialMedia, ProfilePicture, 
    PersonalInfo, SliderText  
)
from .models.about import(
    AboutMe, Review
)
from .models.services import(
    AskedQuestion, Service,
    ServicesTitle
)
from .models.works import(
    WorksTitle, Project
)
from .models.blog import(
    BlogTitle, BlogArticle,
    BlogComment
)
from .models.contact import(
    ContactTitle, UserMessage
)

class SingleInstanceAdmin(admin.ModelAdmin):
    limit_instance_creation = False 

    def has_add_permission(self, request):
            # Jeśli jest co najmniej 1 obiekt, wyłącz możliwość dodawania kolejnego
            if self.limit_instance_creation and self.model.objects.exists():
                return False
            return True

# Index
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


class PersonalInfoAdmin(SingleInstanceAdmin):
    inlines = [SocialMediaInline] #zarządzanie social mediami z poziomu klasy PersonalInfo
    limit_instance_creation = True

   
admin.site.register(MyExpertArea)
admin.site.register(WorkExperience)
admin.site.register(ProfilePicture, ProfilePictureAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(SliderText)


# About
class AboutMeAdmin(SingleInstanceAdmin):
    limit_instance_creation = True

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('uploaded_at',)


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Review, ReviewAdmin)


# Serives 
class ServicesTitleAdmin(SingleInstanceAdmin):
   limit_instance_creation = True
admin.site.register(Service)    
admin.site.register(AskedQuestion)
admin.site.register(ServicesTitle, ServicesTitleAdmin)


# Works
class WorksTitleAdmin(SingleInstanceAdmin):
   limit_instance_creation = True

admin.site.register(WorksTitle, WorksTitleAdmin)    
admin.site.register(Project)


# Blog
class BlogTitleAdmin(SingleInstanceAdmin):
    limit_instance_creation = True

class BlogArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('uploaded_at', 'slug')

class BlogCommentAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'uploaded_at')

admin.site.register(BlogTitle, BlogTitleAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)



# Contact
class ContactTitleAdmin(SingleInstanceAdmin):
    limit_instance_creation = True

class UserMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'phone', 'uploaded_at')

admin.site.register(ContactTitle, ContactTitleAdmin)
admin.site.register(UserMessage, UserMessageAdmin)








