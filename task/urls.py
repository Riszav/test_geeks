
from django.urls import path
from task import views

urlpatterns = [
    path('', views.task_list_api_view),
    path('<int:id>/', views.task_detail_api_view)
]