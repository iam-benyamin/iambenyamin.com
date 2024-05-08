from django.contrib import admin
from user.models import (
    User as UserModel,
    Subscriber as SubscriberModel,
)
from user.admin.subscriber import SubscriberAdmin


admin.site.register(UserModel)
admin.site.register(SubscriberModel, SubscriberAdmin)
