from blog.models import Article as ArticleModel
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from home.forms import ConnectMeForm
from home.models import (
    Address as AddressModel,
    ConnectMe as ConnectMeModel,
    Contact as ContactModel,
    Hero as HeroModel,
    Schedule as ScheduleModel,
    Service as ServiceModel,
    Video as VideoModel,
    ConnectMe as ConnectMeModel,
)
from testimonial.models import Testimonial as TestimonialModel

def home(request):
    context = {
        "address": AddressModel.objects.order_by('-date')[0],
        "contact": ContactModel.objects.order_by('-date')[0],
        "schedule": ScheduleModel.objects.order_by('-date')[0],
        "video": VideoModel.objects.order_by('-date')[0],
        'articles': ArticleModel.objects.order_by('-date')[:3],
        'services': ServiceModel.objects.order_by('-date')[:6],
        'hero': HeroModel.objects.order_by('-date')[0],
        'testimonials': TestimonialModel.objects.all(),
    }
    return render(request, template_name='home/home.html', context=context)



# TODO write connect me form with class base
class ConnectMeFormView(FormView):
    form_class = ConnectMeForm
    template_name = 'home/home.html'
    model = ConnectMeModel
    success_url = reverse_lazy('main:home')


def connect_me_form_view(request):
    if request.method == "GET":
        form = ConnectMeForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('main:home')
