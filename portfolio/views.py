from django.shortcuts import render, redirect
from portfolio.models import Portfolio


# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects.all()
    contents = {"portfolios": portfolios}
    return render(request, "main/portfolio.html", contents)


def add_portfolio(request):
    return render(request, "main/add-portfolio.html")


def portfolio_form(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["PortfolioTitle"]
        logotype = request.POST["PortfolioLogoType"]
        thumbnail = request.FILES["PortfolioThumbnail"]
        Portfolio.objects.create(title=title, logotype=logotype, thumbnail=thumbnail)
        print("새로운 포트폴리오 추가!")
    return redirect("portfolio")
