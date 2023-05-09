from catalog.models import Category, Group, Product
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = UserAdmin.list_display + ("role",)
    fieldsets = UserAdmin.fieldsets + (
        ("Role", {"fields": ["role"]}),
        ("Fixed_category", {"fields": ["fixed_category"]}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Role", {"fields": ["role"]}),
        ("Fixed_category", {"fields": ["fixed_category"]}),
    )


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Category, MyAdmin)
admin.site.register(Product)
admin.site.register(Group)
