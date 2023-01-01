from django.contrib import admin

from portfolio.admin.branch import BranchAdmin
from portfolio.admin.portfolio import PortfolioAdmin

from portfolio.models import (
    Branch as BranchModel,
    Portfolio as PortfolioModel
)

admin.site.register(BranchModel, BranchAdmin)
admin.site.register(PortfolioModel, PortfolioAdmin)
