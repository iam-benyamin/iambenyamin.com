"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import include, path

from blog.sitemaps import ArticleSitemeps
from home.sitemaps import HomeSitemaps
from portfolio.sitemaps import CVSitemaps, PortfolioSitemeps
from links.sitemaps import LinkSitemaps
from config.views import RobotsView


app_name = 'main'

sitemaps = {
    'home': HomeSitemaps,
    'cv': CVSitemaps,
    'links': LinkSitemaps,
    'portfolio': PortfolioSitemeps,
    'blog': ArticleSitemeps,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('links/', include('links.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('robots.txt/', RobotsView.as_view(), name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="dj-sitemaps"),
    path('testimonial/', include('testimonial.urls')),
]

handler404 = "config.views.page_not_found_view"

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
