from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Purchase)
admin.site.register(Order)
admin.site.register(Product)

class Admin(admin.ModelAdmin):
    login_required = False
