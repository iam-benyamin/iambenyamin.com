from django.contrib import admin
from home.admin.address import AdressAdmin
from home.admin.contact import ContactAdmin
from home.admin.hero import HeroAdmin
from home.admin.schedule import ScheduleAdmin
from home.admin.service import ServiceAdmin
from home.admin.video import VideoAdmin
from home.admin.connect_me import ConnectMeAdmin
from home.admin.my_story import MyStoryAdmin

from home.models import (
    Address as AddressModel,
    Contact as ContactModel,
    Hero as HeroModel,
    Schedule as ScheduleModel,
    Service as ServiceModel,
    Video as VideoModel,
    ConnectMe as ConnectMeModel,
    MyStory as MyStoryModel,
)


admin.site.register(AddressModel, AdressAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(ScheduleModel, ScheduleAdmin)
admin.site.register(VideoModel, VideoAdmin)
admin.site.register(HeroModel, HeroAdmin)
admin.site.register(ServiceModel, ServiceAdmin)
admin.site.register(ConnectMeModel, ConnectMeAdmin)
admin.site.register(MyStoryModel, MyStoryAdmin)
