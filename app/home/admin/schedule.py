from django.contrib import admin


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['days', 'time']
