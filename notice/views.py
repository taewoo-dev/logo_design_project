from django.shortcuts import render, redirect


# Create your views here.
def notice(request):
    return render(request, "main/notice.html")


def add_notice(request):
    return render(request, "main/add-notice.html")


def notice_form(request):
    return redirect("notice")
