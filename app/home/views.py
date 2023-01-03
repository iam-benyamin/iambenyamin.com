import requests

from blog.models import Article as ArticleModel
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from rest_framework.generics import ListAPIView

from home.api.serializers import ServiceSerializer
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
    MyStory as MyStoryModel,
)
from portfolio.models import (
    Branch as BranchModel,
    Portfolio as PortfolioModel
)


def home(request):
    context = {
        "address": AddressModel.objects.order_by('-date')[0],
        "contact": ContactModel.objects.order_by('-date')[0],
        "my_story": MyStoryModel.objects.order_by('-date')[0],
        "schedule": ScheduleModel.objects.order_by('-date')[0],
        "video": VideoModel.objects.order_by('-date')[0],
        'articles': ArticleModel.objects.order_by('-date')[:3],
        'services': ServiceModel.objects.order_by('-date')[:6],
        'hero': HeroModel.objects.order_by('-date')[0],
        'branches': BranchModel.objects.order_by('-date'),
        'portfolioes': PortfolioModel.objects.order_by('-date')[:6],
    }
    return render(request, template_name='home/home.html', context=context)


def connect_me_form_view(request):
    if request.method == "POST":
        Token = 'https://console.melipayamak.com/api/send/simple/220260e87e25415a84e4532c7d02fea7'
        form = ConnectMeForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            subject = form.cleaned_data.get('subject')

            print(f'name.lenght {len(name)}')
            print(f'subject.lenght {len(subject)}')
            
            data = {
                'from': '50004001667550',
                'to': '09109667550',    
                'text': f'A person named "{name}" is working with you about the "{subject}"\n\n https://b2n.ir/g57087',
            }
            response = requests.post(Token, json=data)
            messages.success(request, "Hi! I received your message!"
                             " I will try my best to answer you as soon as "
                             "possible. Thank you for your patience"
                             )
            return redirect('/#contact')

        messages.info(request, 'ohhhh!! Something went wrong, please try again! '
                      'Or try other communication methods '
                      'I look forward to receiving your message'
                      )
        return redirect('/#contact')


class ServiceView(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = ServiceModel.objects.all()
