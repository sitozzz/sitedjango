from django.db import models
from product.models import Product

class Status(models.Model):
    name = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Status of the order"
        verbose_name_plural = "Status of orders"


class Order(models.Model):
    # Почта
    order_email = models.EmailField()
    # Контактные данные заказчика
    order_name = models.CharField(max_length=80)
    order_phone = models.CharField(max_length=11, blank=True, null=True, default=None)
    # Время сохдания/ обновления заказа
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # Комментарии к заказу
    commets = models.TextField(blank=True, default=None, null=True)

    status = models.ForeignKey(Status)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ProductInOrder(models.Model):
    # Ссылаемся на таблицу заказа
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    order_email = models.EmailField()
    # Статус заказа
    is_active = models.BooleanField(default=True)
    order_name = models.CharField(max_length=80)
    order_phone = models.CharField(max_length=11, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
