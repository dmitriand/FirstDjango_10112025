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


def get_items(request):
    return HttpResponse("request.path")
