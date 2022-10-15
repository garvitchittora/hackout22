from django.urls import path
from .views import *

urlpatterns = [
    path("", ListCountryAPIView.as_view(), name="todo_list"),
    # path("create/", CreateTodoAPIView.as_view(),name="todo_create"),
    # path("update/<int:pk>/", UpdateTodoAPIView.as_view(),name="update_todo"),
    # path("delete/<int:pk>/", DeleteTodoAPIView.as_view(),name="delete_todo")
]