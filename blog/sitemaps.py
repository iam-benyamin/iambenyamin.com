from django.contrib.sitemaps import Sitemap

from blog.models import Article as ArticleModel


class ArticleSitemeps(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ArticleModel.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return f"blog/detail/{obj.slug}"
