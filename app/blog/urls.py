from django.urls import path

from blog.views import BlogListView, BlogDetailView


app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list-view'),
    path('<slug:pk>/', BlogDetailView.as_view(), name='detail-view'),
]
