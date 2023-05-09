from catalog.views import IndexView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", IndexView.as_view()),
    path("admin/", admin.site.urls),
    path("categories/", include("catalog.urls")),
]
