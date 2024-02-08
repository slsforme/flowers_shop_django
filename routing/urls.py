import uuid
from django.urls import path
from . import views  # импортируем файл из этой же директории
from .views import ProductDelete, ProductUpdate, ProductDetailView, ProductListView, CategoryListView, \
    CategoryDetailView, TagListView, TagDetailView, TagCreateView, OrderDeleteView, OrderUpdateView, OrderListView, \
    OrderDetailView

urlpatterns = [
    path('', views.home, name='Home'),
    path('catalogue/', views.catalogue, name='Flowers Catalogue'),
    path('my-account/', views.my_account, name='Personal Cabinet'),
    path('shopping-cart/', views.shopping_cart, name='Shopping Cart'),
    path('feedback/', views.feedback, name='Feedback'),
    path('api/', views.API_page, name='API'),
    path('change-positions/', views.change_Positions, name='Change Positions'),
    path('create-positions/', views.create_Positions, name='Create Positions'),
    path('delete-positions/', views.delete_Positions, name='Delete Positions'),
    path('read-positions/', views.read_Positions, name='Read Positions'),
    path('signin-signup/', views.sign_page, name='SignIn_SignUp Page'),
    path('user-agreement/', views.agreement_page, name='User Agreement'),
    path('category/<int:category_id>/', views.product_list_by_category, name='Product List'),
    path('tag/<int:tag_id>/', views.product_list_by_tag, name='Products By Tag'),
    path('create-category/', views.create_Categories, name='Create Categories'),
    path('tags/', views.TagListView.as_view(), name="Tags"),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='task-delete'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='task-update'),
    path('detailed-product/<int:pk>', ProductDetailView.as_view(), name='Product Information'),
    path('list-of-products/', ProductListView.as_view(), name='All Products'),
    path('list-of-categories/', CategoryListView.as_view(), name='All Categories'),
    path('detailed-category/<int:pk>', CategoryDetailView.as_view(), name='Category Information'),
    path('detailed-tag/<int:pk>', TagDetailView.as_view(), name='Tag Information'),
    path('create-tags/', views.TagCreateView.as_view(), name="Create Tag"),
    path('create-order/', views.OrderCreateView.as_view(), name='Create Order'),
    path('delete-order/<uuid:pk>', OrderDeleteView.as_view(), name='Delete Order'),
    path('update-order/<uuid:pk>', OrderUpdateView.as_view(), name='Update Order'),
    path('list-of-orders/', OrderListView.as_view(), name='All Orders'),
    path('detailed-order/<uuid:pk>', OrderDetailView.as_view(), name='Order information')
]
