from django.urls import path

from tasks.views import task_list, task_update, task_create, task_delete


app_name = 'tasks'


urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),
]
