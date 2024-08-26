from django.db import models


# Create your models here.
class Column(models.Model):
    title = models.CharField("칼럼 제목", max_length=100)
    content = models.TextField("칼럼 컨텐츠")
    thumbnail = models.ImageField("칼럼 썸네일 이미지", upload_to="column")
    created_at = models.DateTimeField("칼럼 작성 날짜", auto_now_add=True)
