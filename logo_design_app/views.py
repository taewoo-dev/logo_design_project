from django.shortcuts import render

from logo_design_app.models import Post


# Create your views here.

def post_list(requesst):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(requesst, "post_list.html", context)
