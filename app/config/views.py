from django.shortcuts import render
from django.views.generic.base import TemplateView


def page_not_found_view(request, exception):
    return render(request, 'page_not_found_404.html', status=404)


class RobotsView(TemplateView):
    template_name = "robots.txt"
    content_type = "text/plain"
