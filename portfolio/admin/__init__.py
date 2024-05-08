from django.contrib import admin

from portfolio.admin.branch import BranchAdmin
from portfolio.admin.portfolio import PortfolioAdmin
from portfolio.admin.cv import CVAdmin

from portfolio.models import (
    Branch as BranchModel,
    Portfolio as PortfolioModel,
    CV as CVModel,
)

admin.site.register(CVModel, CVAdmin)
admin.site.register(BranchModel, BranchAdmin)
admin.site.register(PortfolioModel, PortfolioAdmin)
