from django.urls import path

from home.views import home, connect_me_form_view

app_name = "main"

urlpatterns = [
    path('', home, name='home'),
    path("submit-connect-to-me-form/", connect_me_form_view, name="connect-me-view"),
]
