from django.contrib import admin


class HeroAdmin(admin.ModelAdmin):
    list_display = ['header', 'text']
    ordering = ('-date',)
