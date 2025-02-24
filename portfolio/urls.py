from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import set_language
from django.conf.urls.static import static
import debug_toolbar


# Ścieżki bez tłumaczenia
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_language/', set_language, name='set_language'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]

# Ścieżki z tłumaczeniem
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('core.urls')),  # <-- Dodaj ścieżkę do aplikacji core
    prefix_default_language=False,  # Ukrywa domyślny język w URL
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
    
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns 
     