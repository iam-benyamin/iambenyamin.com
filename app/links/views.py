from django.views.generic import TemplateView
from django.views.generic.list import ListView

from links.models import Link as LinkModel


class LinkView(ListView):
    template_name = "links/links.html"
    model = LinkModel
