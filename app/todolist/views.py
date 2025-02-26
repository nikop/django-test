from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .forms import TodoItemForm
from todolist.models import TodoItem

def index(request):
    todos = TodoItem.objects.filter(done__isnull=True).order_by("-added")

    if request.method == "POST":
        form = TodoItemForm(request.POST)
    
        if form.is_valid():
            item = TodoItem(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                added = timezone.now()
            )

            item.save()

            return HttpResponseRedirect(reverse("index"))
    else:
        form = TodoItemForm()

    context = {
        "items": todos,
        "form": form,
    }
    return render(request, "index.html", context)

def past(request):
    todos = TodoItem.objects.filter(done__isnull=False).order_by("-done")

    context = {
        "items": todos
    }
    return render(request, "past.html", context)

def view(request, id: int):
    todo = get_object_or_404(TodoItem, pk=id)

    if request.method == "POST":
        if request.POST["action"] == "markdone":
            todo.done = timezone.now()
            todo.save()

            return HttpResponseRedirect(reverse("index"))
        else:
            form = TodoItemForm(request.POST)
        
            if form.is_valid():
                todo.title = form.cleaned_data["title"]
                todo.description = form.cleaned_data["description"]
                todo.modified = timezone.now()

                todo.save()

                return HttpResponseRedirect(reverse("index"))
    else:
        form = TodoItemForm({
            "title": todo.title,
            "description": todo.description,
        })

    context = {
        "item": todo,
        "form": form,
    }

    return render(request, "view.html", context)