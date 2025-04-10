from django.contrib import admin
from django.urls import path,include
from .views import *


app_name="todolist"
urlpatterns = [
    path('', Home,name="home"),
    path('tasks/', get_tasks, name='get_tasks'), 
    path('add-task/', add_task, name='add_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
]