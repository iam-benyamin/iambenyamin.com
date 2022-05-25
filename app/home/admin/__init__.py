from django.contrib import admin

from home.admin.contact import ContactAdmin
from home.admin.schedule import ScheduleAdmin
from home.admin.address import AdressAdmin


from home.models import (
    Address as AddressModel,
    Contact as ContactModel,
    Schedule as ScheduleModel,
)

admin.site.register(AddressModel, AdressAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(ScheduleModel, ScheduleAdmin)
