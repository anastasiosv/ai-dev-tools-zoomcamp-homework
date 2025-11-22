# todos/urls.py
from django.urls import path
from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoToggleResolvedView,
)

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/new/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/edit/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo/<int:pk>/toggle/', TodoToggleResolvedView.as_view(), name='todo_toggle_resolved'),
]