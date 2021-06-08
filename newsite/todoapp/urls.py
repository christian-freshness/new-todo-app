from . import views
from django.urls import path

app_name = 'todoapp'
urlpatterns = [
    #/todoapp/
    path('',views.index,name='index'),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
]