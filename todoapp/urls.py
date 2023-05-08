from django.contrib import admin
from django.urls import include, path
from todoapp.home_view import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('tasks/', include('todoapp.tasks.urls'))
]
