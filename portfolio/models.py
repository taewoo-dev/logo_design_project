from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title = models.CharField("포트폴리오 제목", max_length=100)
    logotype = models.CharField("포트폴리오 로고 종류", max_length=100)
    thumbnail = models.ImageField("포트폴리오 썸네일 이미지", upload_to="portfolio")
    created_at = models.DateTimeField("작성 날짜", auto_now_add=True)
