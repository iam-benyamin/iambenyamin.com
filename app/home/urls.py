from django.urls import path

from home.views import home, connect_me_form_view, ServiceView

app_name = "main"

urlpatterns = [
    path('', home, name='home'),
    path("submit-connect-to-me-form/", connect_me_form_view, name="connect-me-view"),
    path('service-title/', ServiceView.as_view(), name="services-title")
]
