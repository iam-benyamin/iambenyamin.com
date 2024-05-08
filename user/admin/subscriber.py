from django.contrib import admin


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_of_subscribe']
