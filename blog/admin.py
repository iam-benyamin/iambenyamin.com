from django.contrib import admin

from blog.models import Article as ArticleModel


admin.site.register(ArticleModel)
