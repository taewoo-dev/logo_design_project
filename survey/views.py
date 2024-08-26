from django.shortcuts import render, redirect

from survey.models import Survey


# Create your views here.
def survey(request):
    return render(request, "main/survey_form.html")


def survey_form(request):
    if request.method == "POST":
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
        Survey.objects.create(
            username=username,
            phone=phone_number,
            email=email,
            brand_name=brand_name,
            brand_mean=brand_mean,
            brand_desc=brand_desc,
            brand_target=brand_target,
            logo_type=logo_type,
            brand_image=brand_image,
            brand_color=brand_color,
        )
        print("새로운 고객 추가")
    # 견적서를 파일로 변환하는 로직 이후에 추가
    return redirect("main")
