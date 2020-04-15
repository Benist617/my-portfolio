from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('projects.urls')),
    path('todoapp/', include('todoapp.urls')),
    path('pollapp', include('pollapp.urls')),
    path('admin/', admin.site.urls),
]
#check if we in debug and then goes
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
