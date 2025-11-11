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
