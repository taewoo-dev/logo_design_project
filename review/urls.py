from django.urls import path

from review.views import review, review_form

urlpatterns = [
    path("", review, name="review"),
    path("form/", review_form, name="review_form"),
]
