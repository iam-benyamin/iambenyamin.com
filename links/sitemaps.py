from django.contrib.sitemaps import Sitemap

from links.models import Link


class LinkSitemaps(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return ['links:links', ]

    def location(self, item):
        return "links/"
