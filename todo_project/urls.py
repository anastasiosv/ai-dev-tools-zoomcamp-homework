# todo_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')), 
       path('', RedirectView.as_view(pattern_name='todo_list', permanent=False), name='home'),
]