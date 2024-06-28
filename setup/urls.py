from django.contrib import admin
from django.urls import path

from todos.views import TodoListView, TodoCreatView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreatView.as_view(), name="todo_create"),
]
