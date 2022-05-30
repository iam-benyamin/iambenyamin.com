from django.shortcuts import render

from home.models import (
    Address as AddressModel,
    Contact as ContactModel,
    Schedule as ScheduleModel,
    Video as VideoModel,
)
from blog.models import Article as ArticleModel


def home(request):
    context = {
        "address": AddressModel.objects.order_by('-date')[0],
        "contact": ContactModel.objects.order_by('-date')[0],
        "schedule": ScheduleModel.objects.order_by('-date')[0],
        "video": VideoModel.objects.order_by('-date')[0],
        'articles': ArticleModel.objects.order_by('-date')[:3],
    }
    return render(request, template_name='home/home.html', context=context)
