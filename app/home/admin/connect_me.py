from django.contrib import admin


class ConnectMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    list_filter = ('is_read',)
    ordering = ('-date',)
