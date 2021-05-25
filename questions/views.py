from re import L
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import QuestionPaper


class HomeView(LoginRequiredMixin, ListView):
    model = QuestionPaper
    template_name = 'questions/home.html'
    context_object_name = 'papers'


class PaperDetailView(DetailView):
    model = QuestionPaper
    template_name = 'questions/detail.html'
    context_object_name = 'paper'


class PaperCreateView(CreateView):
    model = QuestionPaper
    fields = '__all__'
    template_name = 'questions/create.html'
