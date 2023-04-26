from django.urls import path
from tasks.views import (
    create_task,
    show_my_tasks,
    delete_task,
    create_task_specific,
    show_project,
)

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("<int:id>/delete/", delete_task, name="delete_task"),
    path(
        "<int:id>/create/", create_task_specific, name="create_task_specific"
    ),
]
