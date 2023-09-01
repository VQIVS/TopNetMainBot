from django.urls import path
from .views import post_list
app_name = "api-v1"

urlpatterns = [
    path('post_list/', post_list, name='post_list')
]