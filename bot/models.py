from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email


class Products(models.Model):
    product_id = models.IntegerField(max_length=10)
    link = models.CharField(max_length=255)
    price = models.IntegerField(max_length=255)


class Order(models.Model):
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )

    product_id = models.ForeignKey(
        "Products",
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=255)
    quantity = models.IntegerField()


class Purchase(models.Model):
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )

    product_id = models.ForeignKey(
        "Products",
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=255)
