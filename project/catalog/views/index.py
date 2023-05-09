from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return redirect("/categories")
