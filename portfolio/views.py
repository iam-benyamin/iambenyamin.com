from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from portfolio.models.portfolio import Portfolio
from portfolio.models.CV import CV


class PortfolioListView(ListView):
    model = Portfolio
    paginate_by = 12
    ordering = ['-date']
    template_name = "portfolio/list_view.html"


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/detail_view.html'


class MyCVDetailView(DetailView):
    model = CV
    template_name = 'portfolio/cv_view.html'
