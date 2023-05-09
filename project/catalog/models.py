from django.contrib.auth.models import AbstractUser
from django.db import models
from treebeard.mp_tree import MP_Node


class User(AbstractUser):
    class Role(models.IntegerChoices):
        ADMIN = 1, "Admin"
        MANAGER = 2, "Manager"
        CLIENT = 3, "Client"

        __empty__ = "(Unknown)"

    role = models.IntegerField(
        choices=Role.choices,
        default=Role.CLIENT,
    )
    fixed_category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, blank=True, null=True
    )

    def is_admin(self) -> bool:
        return self.role == self.Role.ADMIN

    def is_manager(self) -> bool:
        return self.role == self.Role.MANAGER


class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"

    def get_child_ids(self) -> list[int]:
        descendants = self.get_descendants()
        return [elem.id for elem in descendants]


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    vendor_code = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Group(models.Model):
    name = models.CharField(max_length=130)
    products = models.ManyToManyField(Product, related_name="groups")

    def __str__(self) -> str:
        return f"{self.name}"
