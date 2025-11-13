from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item

# Create your views here.


# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
#     {"id": 7, "name": "Картофель фри", "quantity": 0},
#     {"id": 8, "name": "Кепка", "quantity": 124},
# ]


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
    item = Item.objects.filter(pk=id)
    if not item:
        return render(
            request, "errors.html", {"errors": [f"Item with id={id} not found"]}
        )
    return render(request, "item.html", context={"item": item})


def get_all_items(request):
    items = Item.objects.all()
    return render(request, "items.html", {"items": items})
