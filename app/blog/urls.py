from django.urls import path

from blog.views import BlogListView


app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list-view'),
]
