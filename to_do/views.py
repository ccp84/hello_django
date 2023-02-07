from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "to_do/todo_list.html", context)
