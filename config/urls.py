"""
URL configuration for config project.

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
from django.conf import settings
from django.contrib import admin
from products.views import products
from django.urls import path, include
from django.conf.urls.static import static
from book import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products),
    path('authors/', book_views.author_list_creation),
    path('', include('book.urls')),
    path('', include('pages.urls')),
    path('auth/', include("django.contrib.auth.urls")),
    path('account/', include("account.urls"))
]

if settings.DEBUG:
    urlpatterns += (
            static(settings.STATIC_URL, document_root=settings.STATIC_ROOT_PATH) +
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
