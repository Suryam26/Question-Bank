from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import QuestionPaper


class HomeView(LoginRequiredMixin, ListView):
    model = QuestionPaper
    template_name = 'questions/home.html'
    context_object_name = 'papers'


class PaperDetailView(LoginRequiredMixin, DetailView):
    model = QuestionPaper
    template_name = 'questions/detail.html'
    context_object_name = 'paper'


class PaperCreateView(LoginRequiredMixin, CreateView):
    model = QuestionPaper
    fields = ['branch', 'subject', 'exam', 'year', 'semester', 'paper']
    template_name = 'questions/create.html'
    success_url = reverse_lazy('mylist')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MyListView(LoginRequiredMixin, ListView):
    model = QuestionPaper
    template_name = 'questions/mylist.html'
    context_object_name = 'mylist'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by('-updated_at')


class PaperUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = QuestionPaper
    fields = ['branch', 'subject', 'exam', 'year', 'semester', 'paper']
    template_name = 'questions/update.html'
    success_url = reverse_lazy('mylist')

    def test_func(self):
        return self.get_object().author == self.request.user


class PaperDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = QuestionPaper
    template_name = 'questions/delete.html'
    context_object_name = 'paper'
    success_url = reverse_lazy('mylist')

    def test_func(self):
        return self.get_object().author == self.request.user
