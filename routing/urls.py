from django.urls import path
from . import views  # импортируем файл из этой же директории

urlpatterns = [
    path('', views.home, name='Home'),
    path('Catalogue', views.catalogue, name='Flowers Catalogue'),
    path('My account', views.my_account, name='Personal Cabinet'),
    path('Shopping Cart', views.shopping_cart, name='Shopping Cart'),
    path('Roses Assortment', views.roses_page, name='Roses assortment'),
    path('Pions Sssortment', views.pions_page, name='Pions assortment'),
    path('Feedback page', views.feedback, name='Feedback'),
    path('API page', views.API_page, name='API'),
    path('Change Positions page', views.change_Positions, name='Change Positions'),
    path('Create Positions page', views.create_Positions, name='Create Positions'),
    path('Delete Positions page', views.delete_Positions, name='Delete Positions'),
    path('Read Positions page', views.read_Positions, name='Read Positions'),
    path('SignIn_SignUp page', views.read_Positions, name='SignIn_SignUp Page'),
    path('Chrysanthemums Assortment page', views.chrysanthemums_page, name='Chrysanthemums Assortment'),
    path('Bouquets Assortment page', views.bouquets_page, name='Bouquets Assortment'),
    path('User Agreement page', views.agreement_page, name='User Agreement')
]
