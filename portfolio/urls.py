from django.urls import path

from portfolio.views import (
    PortfolioListView,
    PortfolioDetailView,
    MyCVDetailView,
)


app_name = 'portfolio'

urlpatterns = [
    path('list/', PortfolioListView.as_view(), name='list-view'),
    path('detail/<slug:slug>/', PortfolioDetailView.as_view(), name='detail-view'),
    # path('<slug:slug>/', MyCVDetailView.as_view(), name='cv-view'),
]
