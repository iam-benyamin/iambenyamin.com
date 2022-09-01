from django.urls import path

from testimonial.views import CreateTestimonails

app_name = "testimonails"

urlpatterns = [
    path("create/", CreateTestimonails.as_view(), name="create-testimonials"),
]
