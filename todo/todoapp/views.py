from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoInputForm

# Create your views here.


def index(request):
    tasks = Todo.objects.all()

    if request.method == "POST":
        form = TodoInputForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TodoInputForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todoapp/index.html', context)


def UpdateTask(request, pk):
    task = Todo.objects.get(id=pk)

    if request.method == "POST":
        form = TodoInputForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TodoInputForm(instance=task)
    context = {'form': form}

    return render(request, 'todoapp/update.html', context)


def DeleteTask(request, pk):
    item = Todo.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(request, 'todoapp/delete.html', context)
