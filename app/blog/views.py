from multiprocessing import get_context
from django.shortcuts import render
from django.views.generic.list import ListView
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/list_view.html'
