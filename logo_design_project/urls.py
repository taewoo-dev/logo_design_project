"""
URL configuration for logo_design_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from logo_design_app.views import post_list, post_detail, post_add, main, survey, portfolio, column, \
    review, notice, survey_form, review_form, add_portfolio
from logo_design_project.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('posts/', post_list),
    path('posts/<int:post_id>/', post_detail),
    path('posts/add/', post_add),

    # 여기서 부터 main url
    path("main", main),
    path("portfolio", portfolio),
    path('survey', survey),
    path("column", column),
    path("review", review),
    path("notice", notice),
    path("add-portfolio/", add_portfolio),
    path('survey-form/', survey_form, name='survey_form'),
    path('review-form/', review_form, name="review_form")
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
