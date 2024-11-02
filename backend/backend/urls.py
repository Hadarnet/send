
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
# Api URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/', include('location.urls')),
    path('user/', include('user.urls')),
    path('chat/', include('chat.urls')),
    path('business/', include('business.urls')),
    path('telecom/', include('telecom.urls')),
    path('sync/', include('sync.urls')),
    path('settings/', include('settings.urls')),
    path('wallet/', include('wallet.urls')),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
