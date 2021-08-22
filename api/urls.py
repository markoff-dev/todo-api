from django.urls import path
from . import views

urlpatterns = [
    path('todos', views.ToDoList.as_view()),
    path('todos/<int:todo_id>', views.ToDoEdit.as_view()),
]
