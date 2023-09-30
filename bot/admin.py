from .models import *


admin.site.register(User)
admin.site.register(Purchase)
admin.site.register(Order)
admin.site.register(Link)
admin.site.register(Email)

class Admin(admin.ModelAdmin):
    login_required = False
