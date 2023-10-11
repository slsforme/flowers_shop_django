from django.urls import path
from . import views  # импортируем файл из этой же директории

urlpatterns = [
    path('', views.home, name='Home'),
    path('catalogue', views.catalogue, name='Flowers Catalogue'),
    path('my_account', views.my_account, name='Personal Cabinet'),
    path('shopping_cart', views.shopping_cart, name='Shopping Cart'),
    path('roses', views.roses_page, name='Roses assortment'),
    path('pions', views.pions_page, name='Pions assortment'),
    path('feedback', views.feedback, name='Feedback'),
    path('API', views.API_page, name='API'),
    path('change_Positions', views.change_Positions, name='Change Positions'),
    path('create_Positions', views.create_Positions, name='Create Positions'),
    path('delete_Positions', views.delete_Positions, name='Delete Positions'),
    path('read_Positions', views.read_Positions, name='Read Positions'),
    path('sign_page', views.read_Positions, name='SignIn_SignUp Page')
]
