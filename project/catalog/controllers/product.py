from catalog.models import Category, Group, Product
from django.db.models import QuerySet
from django.forms import BaseForm
from django.http import HttpRequest


class ProductController:
    filter_components = {
        "__in": ["price", "vendor_code"],
        "__icontains": ["name", "description"],
    }

    def build_filter(self, request: HttpRequest) -> dict:
        _filter = {}
        if request.GET.getlist("groups"):
            _filter["groups__id__in"] = request.GET.getlist("groups")

        for key, val in self.filter_components.items():
            for field in val:
                if request.GET.get(field):
                    if key == "__in":
                        _filter[field + key] = [request.GET.get(field)]
                    else:
                        _filter[field + key] = request.GET.get(field)
        return _filter

    def get_ids_categories(self, category: Category) -> list[int]:
        return [category.id, *category.get_child_ids()]

    def get_products(
        self, ids_categories: list[int], _filter: dict
    ) -> QuerySet[Product]:
        products = Product.objects.filter(category_id__in=ids_categories)
        products = products.filter(**_filter)
        return products.distinct()

    def get_page_data(self, request: HttpRequest, category_id: int) -> dict:
        """get page data"""
        _filter = product_controller.build_filter(request)
        category = Category.objects.get(id=category_id)
        ids_categories = self.get_ids_categories(category)
        products = self.get_products(ids_categories, _filter)
        groups = Group.objects.filter(
            products__category__id__in=ids_categories
        ).distinct()

        return {"products": products, "category": category, "groups": groups}

    def create_product(self, form: BaseForm, category_id: int):
        Product.objects.create(**form.cleaned_data, category_id=category_id)

    def get_product(self, product_id: int) -> Product:
        return Product.objects.get(id=product_id)

    def update_product(self, form: BaseForm, category_id: int, product_id: int):
        Product.objects.filter(id=product_id).update(
            **form.cleaned_data, category_id=category_id
        )

    def delete_product(self, product_id):
        Product.objects.get(id=product_id).delete()


product_controller = ProductController()
