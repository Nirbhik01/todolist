from django.contrib import admin
from django.urls import path,include
from .views import *

# project's urls.py contsins (path("todo/",include("todolist.urls")))
app_name="todolist"
urlpatterns = [
    path('', Home,name="home"),
    path('tasks/', get_tasks_all, name='get_tasks'), 
    path('add-task/', add_task, name='add_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    path("filtertask/",get_tasks,name="filtertask"),
    path('edit-task/<int:task_id>/', edit_task, name='edit_task'),
]