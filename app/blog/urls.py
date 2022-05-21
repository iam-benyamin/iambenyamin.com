from django.urls import path

from blog.views import blog


app_name = 'blog'

urlpatterns = [
    path('', blog, name='list-view')
]
