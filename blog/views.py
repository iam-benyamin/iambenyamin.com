from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Article


class BlogListView(ListView):
    model = Article
    template_name = 'blog/list_view.html'
    paginate_by = 12
    ordering = ['-date']


class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog/detail_view.html'
