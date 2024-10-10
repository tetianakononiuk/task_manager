from django.urls import path
from my_app.views import  SubTaskListCreateView, SubTaskDetailUpdateDeleteView, TaskListCreateView


urlpatterns =[
    path('tasks/', TaskListCreateView.as_view(), name='task_list_create'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask_list_create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask_detail'),
]

