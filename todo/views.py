from django.shortcuts import render, redirect
from .models import Todo

# View to list all the todos
def todo_list(request):
    todos = Todo.objects.order_by('-id')  # Fetch all todos ordered by id in descending order
    return render(request, 'todo/index.html', {'todos': todos})  # Pass the todos to the template

# View to create a new todo
def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']  # Retrieve the title from the POST request
        description = request.POST['description']  # Retrieve the description from the POST request
        Todo.objects.create(title=title, description=description)  # Create and save a new Todo object
    return redirect('todo_list')

# View to mark a todo as completed
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

# View to delete a todo
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
