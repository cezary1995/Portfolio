from .models.index import PersonalInfo, WorkExperience, SliderText
from .models.about import AboutMe
from .models.blog import BlogTitle
from .models.blog import BlogArticle
from .models.services import ServicesTitle, Service
from .models.works import WorksTitle, Project
from .models.contact import ContactTitle
from modeltranslation.translator import register, TranslationOptions


@register(PersonalInfo)
class PersonalInfoTranslationOptions(TranslationOptions):
    fields = ('short_desc',)

@register(AboutMe)
class AboutMeTranslationOptions(TranslationOptions):
    fields = ('content',)

@register(WorkExperience)
class WorkExperienceTranslationOptions(TranslationOptions):
    fields = (
        'position', 
        'job_desc',
    )

@register(BlogTitle)
class BlogTitleTranslationOptions(TranslationOptions):
    fields = ('blog_desc',)

@register(BlogArticle)
class BlogArticleTranslationOptions(TranslationOptions):
    fields = (
        'category', 
        'content',
    )

@register(ServicesTitle)
class ServicesTitleTranslationOptions(TranslationOptions):
    fields = ('serv_desc',)

@register(Service)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(WorksTitle)
class WorksTitleTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'proj_desc',
        'slug',
    )

@register(ContactTitle)
class ContactTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(SliderText)
class SliderTranslationOptions(TranslationOptions):
    fields = ('slider_text',)


