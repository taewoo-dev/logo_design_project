from django.db import models


# Create your models here.
class Review(models.Model):
    content = models.TextField("리뷰 내용")
    rating = models.CharField("평점", max_length=10)
    thumbnail = models.ImageField("리뷰 썸네일 이미지", upload_to="review")
    created_at = models.DateTimeField("작성 날짜", auto_now_add=True)
    updated_at = models.DateTimeField("수정 날짜", auto_now=True)
