from django.shortcuts import render, redirect

from review.models import Review


# Create your views here.
def review(request):
    reviews = Review.objects.all()
    contents = {"reviews": reviews}
    return render(request, "main/review.html", contents)


def review_form(request):
    if request.method == "POST":
        content = request.POST["ReviewContent"]
        rating = request.POST["star"][0]
        image = request.FILES["ReviewThumbnail"]
        Review.objects.create(content=content, rating=rating, thumbnail=image)
        print("새로운 리뷰 추가")
    return redirect("review")
