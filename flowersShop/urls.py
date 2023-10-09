"""
URL configuration for flowersShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('routing.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # добавление подключения всех статических файлов

"""
_Django Documentation_
This helper function works only in debug mode and only if the given prefix is local (e.g. static/) and not a URL (e.g. http://static.example.com/).
Also this helper function only serves the actual STATIC_ROOT folder; it doesn’t perform static files discovery like django.contrib.staticfiles.
"""

