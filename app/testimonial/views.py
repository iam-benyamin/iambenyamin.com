from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from testimonial.forms import TestimonialForm
from testimonial.models import Testimonial as TestimonialModel


class CreateTestimonails(CreateView):
    model = TestimonialModel
    form_class = TestimonialForm
    template_name = "testimonials/create_testimonials.html"
    success_url = reverse_lazy('main:home')
