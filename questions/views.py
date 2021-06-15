from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import QuestionPaper
from .query_set import set_builder


class HomeView(ListView):
    model = QuestionPaper
    template_name = 'questions/home.html'
    context_object_name = 'papers'

    def get_queryset(self):
        filter_set = self.model.objects.all()
        if self.request.GET.get('search'):
            search_text = self.request.GET.get('search')
            filter_set = self.model.objects.search(search_text)
        return set_builder(filter_set)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('search'):
            context['search'] = self.request.GET.get('search')
        return context


class MyListView(LoginRequiredMixin, ListView):
    model = QuestionPaper
    template_name = 'questions/mylist.html'
    context_object_name = 'mylist'

    def get_queryset(self):
        filter_set = self.model.objects.all()
        if self.request.GET.get('search'):
            search_text = self.request.GET.get('search')
            filter_set = self.model.objects.search(search_text)
        return filter_set.filter(author=self.request.user).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('search'):
            context['search'] = self.request.GET.get('search')
        return context


class PaperCreateView(LoginRequiredMixin, CreateView):
    model = QuestionPaper
    fields = ['branch', 'subject', 'exam', 'year', 'semester', 'paper']
    template_name = 'questions/create.html'
    success_url = reverse_lazy('mylist')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


class PaperDetailView(LoginRequiredMixin, DetailView):
    model = QuestionPaper
    template_name = 'questions/detail.html'
    context_object_name = 'paper'
