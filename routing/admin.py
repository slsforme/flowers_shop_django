from django.contrib import admin
from .models import Order, OrderPosition, Product, Category, Tag


# Регистрация моделей в админ - панели
admin.site.register(Order)
admin.site.register(OrderPosition)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
