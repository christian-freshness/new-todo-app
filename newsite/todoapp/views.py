from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.template import loader
from django.utils import timezone
# Create your views here.


def index(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    context = {
        'todo_items': todo_items
    }
    return render(request,'todoapp/index.html', context)


def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    created_object = Todo.objects.create(added_date=current_date, text=content)
    length_of_todos = Todo.objects.all().count()
    print(created_object)
    print(length_of_todos)
    return redirect('todoapp:index')


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('todoapp:index')