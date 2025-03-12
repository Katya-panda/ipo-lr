from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Главная страница</h1><p>Добро пожаловать в магазин масок!</p>")

def author(request):
    return HttpResponse("<h1>Об авторе</h1><p>Лабораторную работу выполнила Поляк Е.</p>")

def about(request):
    return HttpResponse("<h1>О магазине</h1><p>Магазин масок и костюмов для праздников.</p>")


from django.shortcuts import render

def home(request):
    return render(request, 'shop/home.html')  # Возвращает HTML-шаблон для главной страницы

def author(request):
    return render(request, 'shop/author.html')  # Возвращает HTML-шаблон для страницы об авторе

def about(request):
    return render(request, 'shop/about.html')  # Возвращает HTML-шаблон для страницы о магазине

