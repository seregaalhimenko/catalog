from catalog.models import Category
from django.forms import BaseForm
from django.http import HttpRequest


class CategoryController:
    def get_page_data_for_admin(self) -> list:
        return Category.get_annotated_list()

    def get_page_data_for_manager(self, request: HttpRequest) -> list:
        return Category.get_annotated_list(request.user.fixed_category)

    def get_page_data(self, request: HttpRequest) -> dict:
        is_admin = request.user.is_admin()
        if is_admin:
            annotated_list = self.get_page_data_for_admin()
        elif request.user.is_manager():
            annotated_list = self.get_page_data_for_manager(request)
        else:
            annotated_list = []
        return {
            "annotated_list": annotated_list,
            "is_admin": is_admin,
        }

    def create_category_root(self, form: BaseForm):
        name = form.cleaned_data["name"]
        Category.add_root(name=name)

    def create_category_child(self, form: BaseForm, category_id: int):
        name = form.cleaned_data["name"]
        category = Category.objects.get(id=category_id)
        category.add_child(name=name)

    def delete_category(self, category_id: int):
        Category.objects.get(id=category_id).delete()


category_controller = CategoryController()
