from django.contrib import admin

from home.admin.contact import ContactAdmin
from home.admin.schedule import ScheduleAdmin
from home.admin.address import AdressAdmin
from home.admin.video import VideoAdmin


from home.models import (
    Address as AddressModel,
    Contact as ContactModel,
    Schedule as ScheduleModel,
    Video as VideoModel,
)

admin.site.register(AddressModel, AdressAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(ScheduleModel, ScheduleAdmin)
admin.site.register(VideoModel, VideoAdmin)
