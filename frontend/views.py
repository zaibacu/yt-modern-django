from django.views.generic.base import TemplateView

from rest_framework.authtoken.models import Token


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        (token, _) = Token.objects.get_or_create(user=self.request.user)
        context["auth_token"] = token.key
        return context
