from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from portfolio.models import (
    Portfolio as PortfolioModel,
    CV as CVModel,
)


class PortfolioSitemeps(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return PortfolioModel.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return f"portfolio/detail/{obj.slug}"


class CVSitemaps(Sitemap):
    changefreq = 'daily'
    priority = 1
    protocol = 'https'

    def items(self):
        return CVModel.objects.all()[:1]

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return f'portfolio/{obj.slug}'
