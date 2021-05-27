from django.urls import path

from .views import HomeView, PaperDetailView, PaperCreateView, MyListView, PaperUpdateView, PaperDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('paper/<int:pk>/detail/', PaperDetailView.as_view(), name='detail'),
    path('paper/new/', PaperCreateView.as_view(), name='create'),
    path('paper/mylist/', MyListView.as_view(), name='mylist'),
    path('paper/<int:pk>/update', PaperUpdateView.as_view(), name='update'),
    path('paper/<int:pk>/delete', PaperDeleteView.as_view(), name='delete'),
]
