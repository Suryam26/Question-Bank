from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"
