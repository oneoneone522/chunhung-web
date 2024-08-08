from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.views import index, contact

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()