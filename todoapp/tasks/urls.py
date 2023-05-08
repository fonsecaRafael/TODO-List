from django.urls import path
from todoapp.tasks import views


app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home')
]
