from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration\signup.html"
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration\profile.html"
