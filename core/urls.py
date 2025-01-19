import debug_toolbar
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('about/', views.about, name='about'),
     path('services/', views.services, name='services'),
     path('works/', views.works, name='works'),
     path('blog/', views.blog, name='blog'),
     path('contact/', views.contact, name='contact'),
     path('article/<slug:slug>/<int:article_id>/', views.article, name='article'),
] 

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns 