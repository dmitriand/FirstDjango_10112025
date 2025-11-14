from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item

# Create your views here.


def home(request):
    context = {"name": "Иванов Иван Николаевич", "email": "my_mail@mail.ru"}
    return render(request, "index.html", context)


def about(request):
    user = {
        "first_name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    return render(request, "about.html", context={"user": user})


def get_item(request, id):
    try:
        item = Item.objects.get(pk=id)
        colors = item.colors.all()
    except Item.DoesNotExist:
        return render(
            request, "errors.html", {"errors": [f"Item with id={id} not found"]}
        )
    return render(request, "item.html", context={"item": item,"colors": colors})


def get_all_items(request):
    items = Item.objects.all()
    return render(request, "items.html", {"items": items})
