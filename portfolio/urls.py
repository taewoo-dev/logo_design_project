from django.urls import path
from portfolio.views import portfolio, add_portfolio, portfolio_form

urlpatterns = [
    path("", portfolio, name="portfolio"),
    path("add/", add_portfolio, name="add_portfolio"),
    path("form/", portfolio_form, name="portfolio_form"),
]
