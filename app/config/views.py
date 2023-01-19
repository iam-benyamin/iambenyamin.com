from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, 'page_not_found_404.html', status=404)
