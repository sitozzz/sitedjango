from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s " % self.id

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    # Ссылка на продукт
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    # Картинка
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
