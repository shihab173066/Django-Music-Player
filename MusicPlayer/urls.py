"""
URL configuration for MusicPlayer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Imports Django's built-in admin interface.
from django.urls import path, include  # Imports functions to define URL patterns.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Helps serve static files during development.
from django.conf import settings  # Imports project settings.
from django.contrib.staticfiles.urls import static  # Used to serve media files during development.

urlpatterns = [
    path('admin/', admin.site.urls),  # Maps the admin panel to the 'admin/' URL.
    path('', include('APP.urls'))  # Includes URL patterns from the 'APP' application for the base route.
]

# Adds static file URL patterns (CSS, JavaScript, images) during development.
urlpatterns += staticfiles_urlpatterns()

# Serves media files (uploaded by users) during development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
