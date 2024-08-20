from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField("포스트 제목", max_length=100)
    content = models.TextField("포스트 내용")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"


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


class Review(models.Model):
    content = models.TextField("리뷰 내용")
    rating = models.CharField("평점", max_length=10)
    thumbnail = models.ImageField("리뷰 썸네일 이미지", upload_to="review")
    created_at = models.DateTimeField("작성 날짜", auto_now_add=True)
    updated_at = models.DateTimeField("수정 날짜", auto_now=True)


class Portfolio(models.Model):
    title = models.CharField("포트폴리오 제목", max_length=100)
    logotype = models.CharField("포트폴리오 로고 종류", max_length=100)
    thumbnail = models.ImageField("포트폴리오 썸네일 이미지", upload_to="portfolio")
    created_at = models.DateTimeField("작성 날짜", auto_now_add=True)


class Column(models.Model):
    title = models.CharField("칼럼 제목", max_length=100)
    content = models.TextField("칼럼 컨텐츠")
    thumbnail = models.ImageField("칼럼 썸네일 이미지", upload_to="column")
    created_at = models.DateTimeField("칼럼 작성 날짜", auto_now_add=True)