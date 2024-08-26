from django.contrib import admin
from logo_design_app.models import Post, Comment, Survey, Review, Column


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail"]
    pass


@admin.register(Comment)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "thumbnail", "created_at"]
    pass


@admin.register(Column)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ["id", "thumbnail", "created_at"]
    pass
