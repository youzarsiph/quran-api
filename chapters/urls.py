""" URLConf for quran_api.chapters """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quran_api.chapters.views import ChapterViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("chapters", ChapterViewSet, "chapter")


urlpatterns = [
    path("", include(router.urls)),
]
