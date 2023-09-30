from django.contrib import admin
from django.db import models
import datetime


class Link(models.Model):
    link_id = models.CharField(max_length=255, default="none")
    link = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.link


class Email(models.Model):
    address = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.address


class User(models.Model):
    user_id = models.IntegerField()
    primary_email = models.EmailField(max_length=255, unique=True, blank=True, default="12@gmal.com")
    emails = models.ManyToManyField('Email', blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True, null=True)

    def __str__(self):
        return str(self.user_id)


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders_by_user")
    username = models.CharField(max_length=255, default="name")
    link_id = models.IntegerField()
    email = models.ForeignKey(Email, on_delete=models.CASCADE, related_name="orders_by_email")
    status = models.CharField(max_length=255)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True, null=True)

    def __str__(self):
        return str(self.user_id)


class Admin(admin.ModelAdmin):
    login_required = True



