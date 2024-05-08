from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.generics import ListAPIView

from testimonial.api.serializers import TestimonialSerializer
from testimonial.forms import TestimonialForm
from testimonial.models import Testimonial as TestimonialModel


class CreateTestimonail(CreateView):
    model = TestimonialModel
    form_class = TestimonialForm
    template_name = "testimonials/create_testimonials.html"
    success_url = reverse_lazy('main:home')


class TestimonailView(ListAPIView):
    serializer_class = TestimonialSerializer
    queryset = TestimonialModel.objects.all()
