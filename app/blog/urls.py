from django.urls import path

from blog.views import BlogListView, BlogDetailView


app_name = 'blog'

urlpatterns = [
    path('list/', BlogListView.as_view(), name='list-view'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail-view'),
]
