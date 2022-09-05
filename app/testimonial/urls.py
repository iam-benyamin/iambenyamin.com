from django.urls import path

from testimonial.views import TestimonailView, CreateTestimonail

app_name = "testimonails"

urlpatterns = [
    path('', TestimonailView.as_view(), name="testimonial"),
    path("create/", CreateTestimonail.as_view(), name="create-testimonials"),
]
