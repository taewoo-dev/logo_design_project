# Generated by Django 4.2.15 on 2024-08-26 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="리뷰 내용")),
                ("rating", models.CharField(max_length=10, verbose_name="평점")),
                (
                    "thumbnail",
                    models.ImageField(
                        upload_to="review", verbose_name="리뷰 썸네일 이미지"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성 날짜"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정 날짜"),
                ),
            ],
        ),
    ]
