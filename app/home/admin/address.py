from django.contrib import admin


class AdressAdmin(admin.ModelAdmin):
    list_display = ['address', 'country']
