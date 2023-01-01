from django.contrib import admin


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'branch']
    ordering = ('-date',)
