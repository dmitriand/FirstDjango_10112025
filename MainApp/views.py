from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

user = {
    "first_name": "Иван",
    "middle_name": "Петрович",
    "last_name": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru",
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Дмитриев А.А.</i>
    """
    return HttpResponse(text)


def about(request):
    text = f"""
    Имя: {user["first_name"]}<br>
    Отчество: {user["middle_name"]}<br>
    Фамилия: {user["last_name"]}<br>
    телефон: {user["phone"]}<br>
    email: {user["email"]}
    """
    return HttpResponse(text)


def get_items(request, id):
    found_item = None
    for item in items:
        if item.get("id") == int(id):
            found_item = item
    if id == "10" and not found_item:
        text = "Товар с id=10 не найден"
    else:
        text = f"""
        Товар: {found_item["name"]} <br>
        Количество: {found_item["quantity"]}
        """
    return HttpResponse(text)


def get_all_items(request):
    numbered_list = [f"{i+1}. {item.get("name")}" for i, item in enumerate(items)]
    text = "<br>".join(numbered_list)
    return HttpResponse(text)
