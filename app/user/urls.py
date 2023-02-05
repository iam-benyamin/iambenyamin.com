from django.urls import path

from user.views import subscribe_email_view


app_name = 'user'

urlpatterns = [
    path('subscribe-email/', subscribe_email_view, name="subscribe-email"),
]
