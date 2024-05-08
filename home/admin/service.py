from django.contrib import admin


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    ordering = ('-date',)
