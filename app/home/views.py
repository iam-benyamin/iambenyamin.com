from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'is': 'yes'
    }
    return render(request, template_name='home/home.html', context=context)