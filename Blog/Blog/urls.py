from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from App.views import index, blog,post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),#
    path('blog/', blog),
    path('post/', post),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
