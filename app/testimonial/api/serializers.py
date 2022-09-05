from rest_framework.serializers import ModelSerializer
from testimonial.models import Testimonial


class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        exclude = ['created_at']
