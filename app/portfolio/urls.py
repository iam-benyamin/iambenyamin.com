from django.urls import path

from portfolio.views import PortfolioListView, PortfolioDetailView


app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListView.as_view(), name='list-view'),
    path('<slug:pk>/', PortfolioDetailView.as_view(), name='detail-view'),
]
