from django import forms

from testimonial.models import Testimonial as TestimonialModel


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = TestimonialModel
        fields = "__all__"


