import time
from django import forms
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from core.utils import change_text_field_to_ck
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


class PersonalInfoAdmin(SingleInstanceAdmin, TranslationAdmin):
    inlines = [SocialMediaInline] #zarządzanie social mediami z poziomu klasy PersonalInfo
    limit_instance_creation = True


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ckeditor_fields = ['job_description']
        for field in ckeditor_fields:
            change_text_field_to_ck(fields=self.fields, field=field)

class WorkExperienceAdmin(TranslationAdmin):
    form =  WorkExperienceForm  

class SliderTextAdmin(TranslationAdmin,admin.ModelAdmin):
    pass

admin.site.register(MyExpertArea)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(ProfilePicture, ProfilePictureAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(SliderText, SliderTextAdmin)


# About
class AboutMeAdmin(SingleInstanceAdmin, TranslationAdmin):
    limit_instance_creation = True

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('uploaded_at',)


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Review, ReviewAdmin)


# Serives 
class ServicesTitleForm(forms.ModelForm):
    class Meta:
        model = ServicesTitle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ckeditor_fields = ['serv_desc']
        for field in ckeditor_fields:
            change_text_field_to_ck(fields=self.fields, field=field)


class ServicesTitleAdmin(SingleInstanceAdmin, TranslationAdmin):
    limit_instance_creation = True
    form =  ServicesTitleForm

class ServiceAdmin(TranslationAdmin, admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)    
admin.site.register(AskedQuestion)
admin.site.register(ServicesTitle, ServicesTitleAdmin)


# Works
class ServicesTitleForm(forms.ModelForm):
    class Meta:
        model = WorksTitle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ckeditor_fields = ['desc']
        for field in ckeditor_fields:
            change_text_field_to_ck(fields=self.fields, field=field)

class WorksTitleAdmin(SingleInstanceAdmin, TranslationAdmin):
    limit_instance_creation = True
    form = ServicesTitleForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model = WorksTitle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ckeditor_fields = ['proj_desc']
        for field in ckeditor_fields:
            change_text_field_to_ck(fields=self.fields, field=field)

class ProjectAdmin(TranslationAdmin, admin.ModelAdmin):
    # readonly_fields = ('slug',)
    form = ProjectForm
   
admin.site.register(WorksTitle, WorksTitleAdmin)    
admin.site.register(Project, ProjectAdmin)


# Blog
### blog title
class BlogTitleForm(forms.ModelForm):
    class Meta:
        model = BlogTitle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ckeditor_fields = ['blog_desc',]
        for field in ckeditor_fields:
            change_text_field_to_ck(fields=self.fields, field=field)


class BlogTitleAdmin(SingleInstanceAdmin, TranslationAdmin):
    limit_instance_creation = True
    form = BlogTitleForm

### blog article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = BlogArticle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ckeditor_fields = ['content']
        for field in ckeditor_fields:
            change_text_field_to_ck(fields=self.fields, field=field)

class BlogCommentInLine(admin.TabularInline):
    model = BlogComment
    extra = 0
    fields = ['name', 'email', 'message', 'uploaded_at']
    readonly_fields = ['uploaded_at']

class BlogArticleAdmin(TranslationAdmin, admin.ModelAdmin):
    inlines = [BlogCommentInLine]
    form = ArticleForm
    list_display = ('title',)
    readonly_fields = ('uploaded_at', 'slug')

admin.site.register(BlogTitle, BlogTitleAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)




# Contact
class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = ContactTitle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ckeditor_fields = ['desc']
        for field in ckeditor_fields:
            change_text_field_to_ck(fields=self.fields, field=field)

class ContactTitleAdmin(SingleInstanceAdmin, TranslationAdmin):
    limit_instance_creation = True
    form = ContactAdminForm

class UserMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'phone', 'uploaded_at')

admin.site.register(ContactTitle, ContactTitleAdmin)
admin.site.register(UserMessage, UserMessageAdmin)








