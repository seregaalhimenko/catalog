from catalog.controllers.category import category_controller
from catalog.forms import CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views import View

from .base import Base


class CategoryView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            "categories.html",
            {"form": CategoryForm(), **category_controller.get_page_data(request)},
        )

    def post(self, request):
        if not request.user.is_admin():
            raise PermissionDenied()
        form = CategoryForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                "categories.html",
                {
                    "annotated_list": category_controller.get_page_data_for_admin,
                    "form": CategoryForm(),
                    "context": "Ошибка",
                },
            )
        category_controller.create_category_root(form)
        return redirect("/categories")


class CategoryDetailView(LoginRequiredMixin, Base):
    http_method_names = ["get", "post", "delete"]
    redirect_url = "/categories"

    def get(self, request, category_id):
        return render(request, "form.html", {"form": CategoryForm()})

    def post(self, request, category_id):
        form = CategoryForm(request.POST)
        if not form.is_valid():
            return render(request, "form.html", {"form": form, "context": "Ошибка"})
        category_controller.create_category_child(form, category_id)
        return redirect(self.redirect_url)

    def delete(self, request, category_id):
        category_controller.delete_category(category_id)
        return redirect(self.redirect_url)
