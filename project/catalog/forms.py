from catalog.models import Category, Product
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ("role", "fixed_category")


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserCreationForm.Meta.fields + ("role", "fixed_category")


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["category"]
