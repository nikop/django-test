from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from todolist.models import TodoItem

def index(request):
    todos = TodoItem.objects.filter(done__isnull=True).order_by("-added")

    context = {
        "items": todos
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

    context = {
        "item": todo
    }
    return render(request, "view.html", context)

def markdone(request, id: int):
    todo = get_object_or_404(TodoItem, pk=id)

    todo.done = timezone.now()
    todo.save()

    return HttpResponseRedirect(reverse("index"))

def create(request):

    if request.POST["title"] == "" or request.POST["description"] == "":
        return HttpResponse("Title or Description Missing", status=422)

    item = TodoItem(
        title = request.POST["title"],
        description = request.POST["description"],
        added = timezone.now()
    )

    item.save()

    return HttpResponseRedirect(reverse("index"))