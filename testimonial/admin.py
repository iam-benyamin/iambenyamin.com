from django.contrib import admin

from testimonial.models import Testimonial as TestimonialModel


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_position', 'get_description']
    ordering = ('-created_at',)

    def get_description(self, obj):
        return obj.description[:60]


admin.site.register(TestimonialModel, TestimonialAdmin)
