from django.contrib import admin
from .models import *


admin.site.register(User, Products, Order, Purchase)
