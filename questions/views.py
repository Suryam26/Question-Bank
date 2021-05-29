from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import QuestionPaper


class HomeView(LoginRequiredMixin, ListView):
    model = QuestionPaper
    template_name = 'questions/home.html'
    context_object_name = 'papers'

    def get_queryset(self):
        filter_set = self.model.objects.all()
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            query = Q(subject__subject_name__icontains=search) | Q(
                subject__subject_name_short__icontains=search)
            filter_set = self.model.objects.filter(query)

        query_set = filter_set.values(
            'branch__name', 'subject__subject_name', 'exam', 'year', 'semester', 'paper',).order_by('-year')
        papers = {}
        for i in query_set:
            if i['year'] not in papers:
                papers[i['year']] = []
            papers[i['year']].append(i)
        return papers.items()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('search'):
            context['search'] = self.request.GET.get('search')
        return context


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
        filter_set = self.model.objects.all()
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            query = Q(subject__subject_name__icontains=search) | Q(
                subject__subject_name_short__icontains=search)
            filter_set = self.model.objects.filter(query)

        return filter_set.filter(author=self.request.user).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('search'):
            context['search'] = self.request.GET.get('search')
        return context


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
