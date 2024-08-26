from django.contrib import admin

from column.models import Column


# Register your models here.
@admin.register(Column)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ["id", "thumbnail", "created_at"]
    pass
