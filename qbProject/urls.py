from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin
    path('this-is-not-admin/', admin.site.urls),

    # Smart Select
    path('chaining/', include('smart_selects.urls')),

    # User
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),

    # Question App
    path('', include('questions.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
