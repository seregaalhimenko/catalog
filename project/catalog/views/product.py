from catalog.controllers.product import product_controller
from catalog.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from .base import Base


class ProductView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, category_id: int) -> HttpResponse:
        return render(
            request,
            "products.html",
            {
                "form": ProductForm(),
                **product_controller.get_page_data(request, category_id),
            },
        )

    def post(
        self, request: HttpRequest, category_id: int
    ) -> HttpResponse | HttpResponseRedirect:
        form = ProductForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                "form.html",
                {
                    "form": form,
                    "context": "Ошибка",
                    **product_controller.get_page_data(request, category_id),
                },
            )
        product_controller.create_product(form, category_id)
        return redirect(f"/categories/{category_id}/products/")


class ProductDetailView(LoginRequiredMixin, Base):
    def get(
        self, request: HttpRequest, category_id: int, product_id: int
    ) -> HttpResponse:
        product = product_controller.get_product(product_id)
        form = ProductForm(instance=product)
        return render(
            request,
            "product_detail.html",
            {
                "product_form": form,
                "groups": product.groups.values("name"),
            },
        )

    def post(
        self, request: HttpRequest, category_id: int, product_id: int
    ) -> HttpResponse | HttpResponseRedirect:
        form = ProductForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                "product_detail.html",
                {
                    "product_form": form,
                    "context": "Ошибка",
                },
            )
        product_controller.update_product(form, category_id, product_id)
        return redirect(f"/categories/{category_id}/products/")

    def delete(
        self, request: HttpRequest, category_id: int, product_id: int
    ) -> HttpResponseRedirect:
        product_controller.delete_product(product_id)
        return redirect(f"/categories/{category_id}/products/")
