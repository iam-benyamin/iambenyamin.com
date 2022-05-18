from django.urls import path

from home.views import home

app_name = "main"

urlpatterns = [
    path('', home, name='home')
]
