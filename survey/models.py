from django.db import models

# Create your models here.


class Survey(models.Model):
    username = models.CharField("고객 이름", max_length=100)
    phone = models.CharField("고객 번호", max_length=100)
    email = models.EmailField("고객 이메일")
    brand_name = models.CharField("브랜드 이름", max_length=100)
    brand_mean = models.TextField("브랜드 의미")
    brand_desc = models.TextField("브랜드 묘사")
    brand_target = models.TextField("고객 타겟층")
    logo_type = models.CharField("로고 종류", max_length=100)
    brand_image = models.TextField("넣고 싶은 이미지", max_length=300)
    brand_color = models.CharField("원하는 싶은 색상", max_length=300)
    created_at = models.DateTimeField("작성 날짜", auto_now_add=True)

    def __str__(self):
        return f"{self.username}의 설문지"
