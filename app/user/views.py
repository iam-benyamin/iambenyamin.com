from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect

from user.forms import SubscriberForm


def subscribe_email_view(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()

            email_addr = form.cleaned_data.get('email')
            send_mail(
                subject='subscribe',
                message='',
                html_message='Hi, you are very welcome<br />'
                        'Here I try to publish useful articles in the field of computer and programming<br />'
                        'List of my current <a href="https://iambenyamin.com/blog/list/">articles</a>.<br />'
                        'I hope you like it<br />'
                        'And if you want to communicate with me, you can use this email or use <a href="https://iambenyamin.com/#contact">this form</a>.<br /><br />'
                        '<p style="color: #696969; font-size: 12px; margin-bottom: -4px;">Benyamin Mahmoudyan</p>'
                        '<a href="https://iambenyamin.com" style="color:#696969;font-size:12px;display: inline-block;">iambenyamin.com</a><br />',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[str(email_addr), ],
            )
    return redirect('main:home')
