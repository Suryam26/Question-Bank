from django.urls import path

from .views import HomeView, PaperDetailView, PaperCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/detail/', PaperDetailView.as_view(), name='detail'),
    path('create/', PaperCreateView.as_view(), name='create')
]
