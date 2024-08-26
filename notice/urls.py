from django.urls import path

from notice.views import notice, add_notice, notice_form

urlpatterns = [
    path("", notice, name="notice"),
    path("add/", add_notice, name="add_notice"),
    path("form/", notice_form, name="notice_form"),
]
