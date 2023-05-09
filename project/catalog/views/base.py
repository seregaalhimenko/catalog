from django.views import View


class Base(View):
    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get("_method", "").lower()
        if method == "delete":
            return self.delete(*args, **kwargs)
        return super().dispatch(*args, **kwargs)
