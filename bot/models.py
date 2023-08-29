from django.db import models
from django.contrib import admin


class User(models.Model):
    user_id = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email


class Product(models.Model):
    product_id = models.IntegerField()
    link = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.link


class Order(models.Model):
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )

    product_id = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=255)
    quantity = models.IntegerField()


class Purchase(models.Model):
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )

    purchase_id = models.CharField(max_length=255, default="none")

    product_id = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=255)


class Admin(admin.ModelAdmin):
    login_required = True
