from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'routing/home.html')  # показывает, какой шаблон необходимо показать при переходе
    # пользователя на данную страницу


def catalogue(request):
    return render(request, 'routing/catalogue.html')


def my_account(request):
    return render(request, 'routing/my_account.html')


def shopping_cart(request):
    return render(request, 'routing/shopping_cart.html')


def roses_page(request):
    return render(request, 'routing/flowers_assortment/roses.html')


def pions_page(request):
    return render(request, 'routing/flowers_assortment/roses.html')


def feedback(request):
    return render(request, 'routing/feedback.html')


def API_page(request):
    return render(request, 'routing/API_page.html')


def change_Positions(request):
    return render(request, 'routing/CRUD_pages/change_Positions.html')


def create_Positions(request):
    return render(request, 'routing/CRUD_pages/create_Positions.html')


def delete_Positions(request):
    return render(request, 'routing/CRUD_pages/delete_Positions.html')


def read_Positions(request):
    return render(request, 'routing/CRUD_pages/read_Positions.html')


def sign_page(request):
    return render(request, 'routing/sign_page.html')


def chrysanthemums_page(request):
    return render(request, 'routing/flowers_assortment/chrysanthemums.html')


def bouquets_page(request):
    return render(request, 'routing/flowers_assortment/bouquets.html')


def agreement_page(request):
    return render(request, 'routing/user_agreement.html')
