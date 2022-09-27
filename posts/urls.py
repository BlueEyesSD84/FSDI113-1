from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostListView,
    PostDeleteView,
    PostUpdateView,
    HomePageView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('',HomePageView.as_view(),name='index'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name = 'edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'delete'),
]