
from django.contrib import admin


class CVAdmin(admin.ModelAdmin):
    list_display = ['slug']
