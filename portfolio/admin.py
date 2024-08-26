from django.contrib import admin
from portfolio.models import Portfolio

# Register your models here.


@admin.register(Portfolio)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail"]
    pass
