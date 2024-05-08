from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class HomeSitemaps(Sitemap):
    changefreq = 'daily'
    priority = 1
    protocol = 'https'

    def items(self):
        return ['main:home', ]

    def location(self, item):
        return ""
