from django.contrib import admin


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ('-date',)
