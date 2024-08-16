from django.shortcuts import render, redirect

from logo_design_app.models import Post, Comment, Survey


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_content = request.POST["comment"]
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    context = {
        "post": post
    }
    return render(request, "post_detail.html", context)


def post_add(request):
    if request.method == "POST":
        print("method POST")
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]
        post = Post.objects.create(title=title, content=content, thumbnail=thumbnail)
        return redirect(f"/posts/{post.id}")
    else:
        print("method GET")

    return render(request, "post_add.html")


def main(requset):
    return render(requset, "index2.html")


def survey(request):
    return render(request, "survey_form.html")


def submit_form(request):
    # if request.method == "POST":
    #     req = request.POST
    #     name = req["Name"]
    #     email = req["Email"]
    #     message = req["Message"]
    # print(request.POST)
    username = request.POST["UserName"]
    phone_number = request.POST["Phone"]
    email = request.POST["Email"]
    brand_name = request.POST["BrandName"]
    brand_mean = request.POST["BrandMean"]
    brand_desc = request.POST["BrandDesc"]
    brand_target = request.POST["BrandTarget"]
    logo_type = request.POST["radio"]
    brand_image = request.POST["BrandPlusImage"]
    brand_color = request.POST["BrandColor"]
    Survey.objects.create(username=username, phone=phone_number, email=email, brand_name=brand_name,
                          brand_mean=brand_mean, brand_desc=brand_desc, brand_target=brand_target, logo_type=logo_type,
                          brand_image=brand_image, brand_color=brand_color)
    print("새로운 고객 추가")
    return redirect("/main")
