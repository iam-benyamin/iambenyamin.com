from django.contrib import admin


class MyStoryAdmin(admin.ModelAdmin):
    list_display = ['who_i_am', 'my_vision', 'my_history']
