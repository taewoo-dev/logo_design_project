from django.urls import path

from column.views import column, add_column, column_form, column_detail

urlpatterns = [
    path("", column, name="column"),
    path("add/", add_column, name="add_column"),
    path("<int:column_id>/", column_detail, name="column_detail"),
    path("form/", column_form, name="column_form"),
]
