from django.contrib import admin


class VideoAdmin(admin.ModelAdmin):
    ordering = ('-date',)
