from django.urls import path

from survey.views import survey, survey_form

urlpatterns = [
    path("", survey, name="survey"),
    path("form/", survey_form, name="survey_form"),
]
