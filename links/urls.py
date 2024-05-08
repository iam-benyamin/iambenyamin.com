from django.urls import path

from links.views import LinkView

app_name = "links"

urlpatterns = [
    path('', LinkView.as_view(), name='links'),
]
