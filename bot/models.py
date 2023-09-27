from django.db import models
from django.contrib import admin


class Link(models.Model):
    link_id = models.IntegerField()
    link = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.link


class User(models.Model):
    user_id = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.email


class Order(models.Model):
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )

    link_id = models.ForeignKey(
        "Link",
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

    link_id = models.ForeignKey(
        "Link",
        on_delete=models.CASCADE
    )

#     status = models.CharField(max_length=255)


class Admin(admin.ModelAdmin):
    login_required = True
