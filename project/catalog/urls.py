from catalog.views import (
    CategoryDetailView,
    CategoryView,
    ProductDetailView,
    ProductView,
)
from django.urls import path

urlpatterns = [
    path("", CategoryView.as_view()),
    path("<int:category_id>/products/", ProductView.as_view()),
    path(
        "<int:category_id>/products/<int:product_id>/",
        ProductDetailView.as_view(),
    ),
    path("<int:category_id>/", CategoryDetailView.as_view()),
]
