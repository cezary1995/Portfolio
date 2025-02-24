
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from django.conf.urls.i18n import i18n_patterns
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path(_('about/'), views.about, name='about'),
     path(_('services/'), views.services, name='services'),
     path(_('works/'), views.works, name='works'),
     path(_("project-details/<slug:slug>/"), views.project_details, name='project_details'),
     path(_('blog/'), views.blog, name='blog'),
     path(_('contact/'), views.contact, name='contact'),
     path(_('article') + '/<slug:slug>/<int:article_id>/', views.article, name='article'),
] 

