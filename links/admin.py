from django.contrib import admin
from links.models import Link as LinkModel


class LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'links']


admin.site.register(LinkModel, LinkAdmin)
