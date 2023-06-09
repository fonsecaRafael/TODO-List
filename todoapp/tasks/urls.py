from django.urls import path
from todoapp.tasks import views


app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:task_id>', views.detail, name='detail'),
    path('del/<int:task_id>', views.delete, name='delete'),
]
