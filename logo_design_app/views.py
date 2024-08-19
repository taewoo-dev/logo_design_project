from django.shortcuts import render, redirect

from logo_design_app.models import Post, Comment, Survey, Review, Portfolio


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "sample/post_list.html", context)


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
    return render(request, "sample/post_detail.html", context)


def post_add(request):
    if request.method == "POST":
        print("method POST")
        print(request.FILES)
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]
        post = Post.objects.create(title=title, content=content, thumbnail=thumbnail)
        return redirect(f"/posts/{post.id}")
    else:
        print("method GET")

    return render(request, "sample/post_add.html")


# 여기서 부터 main logo_design_view

def main(request):
    return render(request, "main/index.html")


def portfolio(request):
    portfolios = Portfolio.objects.all()
    contents = {
        "portfolios": portfolios
    }
    return render(request, "main/portfolio.html", contents)


def survey(request: object) -> object:
    return render(request, "main/survey_form.html")


def column(request):
    return render(request, "main/column.html")


def review(request):
    reviews = Review.objects.all()
    print(reviews)
    contents = {
        "reviews": reviews
    }
    return render(request, "main/review.html", contents)


def notice(request):
    return render(request, "main/notice.html")


def add_portfolio(request):
    return render(request, "main/add-portfolio.html")


def portfolio_form(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST['PortfolioTitle']
        logotype = request.POST['PortfolioLogoType']
        thumbnail = request.FILES['PortfolioThumbnail']
        Portfolio.objects.create(title=title, logotype=logotype, thumbnail=thumbnail)
        print("새로운 포트폴리오 추가!")
    return redirect("portfolio")


def survey_form(request):
    if request.method == "POST":
        print(request.POST)
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
                              brand_mean=brand_mean, brand_desc=brand_desc, brand_target=brand_target,
                              logo_type=logo_type,
                              brand_image=brand_image, brand_color=brand_color)
        print("새로운 고객 추가")
    # 견적서를 파일로 변환하는 로직 이후에 추가
    return redirect("main")


def review_form(request):
    if request.method == "POST":
        print(request.POST)
        content = request.POST["ReviewContent"]
        rating = request.POST["star"][0]
        print(request.FILES)
        image = request.FILES['ReviewThumbnail']
        Review.objects.create(content=content, rating=rating, thumbnail=image)
        print("새로운 리뷰 추가")
    return redirect("review")
