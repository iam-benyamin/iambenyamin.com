from django.urls import path

from home.views import home, ConnectMeFormView, connect_me_form_view

app_name = "main"

urlpatterns = [
    path('', home, name='home'),
    path("submit-connect-to-me-form/", ConnectMeFormView.as_view(), name="connect-me-view"),
    # path("submit-connect-to-me-form/", connect_me_form_view, name="connect-me-view"),
]
