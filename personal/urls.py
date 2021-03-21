from django.urls import path
from personal import views

urlpatterns = [
    path("", views.home, name="home"),

    path("add/Task", views.add_task, name = "add_day_task"),
    path("update/Task", views.update_task, name = "update_day_task"),

    path("task/<int:groupid>", views.task, name = "task"),
    path("group/add/task", views.group_add_task, name = "group_add_task"),
    path("group/update/task", views.group_update_task, name = "group_update_task"),
    path("group/edit/task", views.group_edit_task, name = "group_edit_task"),
    path("group/addGroupTask", views.add_group_task, name = "add_group_task"),

    #review
    path("review/day/<int:dId>", views.review_day, name ="review_day"),
    path("utils/task/delete", views.delete_task, name = "delete_task")
]