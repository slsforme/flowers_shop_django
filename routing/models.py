import uuid
from django.core.validators import RegexValidator
from django.db import models


# from phonenumber_field.modelfields import PhoneNumberField

class baseInfo(models.Model):  # абстрактная модель
    name = models.CharField(max_length=255, default='Без названия')
    description = models.CharField(max_length=1024, default='Без описания')

    class Meta:
        abstract = True


class Tag(baseInfo):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text="Имя тэга")
    description = models.CharField(max_length=1024, help_text="Описание тэга", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги'


class Category(baseInfo):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Имя категории")
    description = models.CharField(max_length=1024, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='Без названия', verbose_name='Имя продукта')
    price = models.FloatField(verbose_name="Цена продукта", default=0.0)
    quantity = models.IntegerField(verbose_name="Количество", default=0)
    image = models.ImageField(verbose_name="Фотография", upload_to='flowers_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Время создания продукта")
    changed_at = models.DateTimeField(auto_now=True, help_text="Время изменения продукта")
    is_deleted = models.BooleanField(default=False, verbose_name='Удалена?')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def delete(self, *args, **kwargs):  # Логическое удаление - при вызове данного метода is_deleted меняется на True
        self.is_deleted = True  # и модель будет логически удалена
        self.save()  # Сохраняем объект

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цветы'
        verbose_name_plural = 'Цветы'
        ordering = ['-price']  # Сортировка по убыванию


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)  # также можно реализовать с помощью AutoField
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано в", help_text="Время создания модели")
    deliver_address = models.CharField(max_length=255, verbose_name="Адрес доставки", help_text="Адрес доставки заказа")
    # phone_number = PhoneNumberField(help_text="Мобильный номер телефона клиента", max_length=11)  # RU номер телефона
    phone_regex = RegexValidator(regex=r'^((7|8)+([0-9]){10})$')  # regex для RU номера телефона
    phone_number = models.CharField(validators=[phone_regex], verbose_name="Номер телефона", max_length=11,
                                    # Валидатор должен быть листом
                                    error_messages="Номер телефона не является российским номером или же неправильно "
                                                   "набран")
    product = models.ManyToManyField('Product', through='OrderPosition', related_name='order_positions')

    def __str__(self):
        return f"Заказ {self.id}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class OrderPosition(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', verbose_name="Заказ", on_delete=models.CASCADE)
    product = models.ForeignKey('Product', verbose_name="Продукт", on_delete=models.CASCADE)
    quantity_of_products = models.PositiveIntegerField(default=0, verbose_name="Количество продуктов",
                                                       help_text="Количество позиций в заказе")
    discount_per_single_product = models.FloatField(default=0.0, verbose_name="Скидка за единицу товара",
                                                    help_text="Скидка за единицу товара")

    class Meta:
        verbose_name = 'Позиции заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return f"Позиция Заказа"
