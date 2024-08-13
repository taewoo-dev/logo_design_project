from django.contrib import admin
from logo_design_app.models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class Admin(admin.ModelAdmin):
    pass
