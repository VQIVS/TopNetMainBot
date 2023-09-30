from django.urls import path, include
from .views import ModelViewSetLinks, ModelViewSetUser
from .views import ModelViewSetLinks, ModelViewSetUser, ModelViewSetOrder, ModelViewSetEmail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('links', ModelViewSetLinks, basename="links-api")
router.register('Users', ModelViewSetUser, basename="Users-api")
router.register('Orders', ModelViewSetOrder, basename="Orders-api")
router.register('Emails', ModelViewSetEmail, basename="Emails-api")

app_name = "api-v1"

urlpatterns = [
    # path('post_list/', post_list, name='post_list')
    path('', include(router.urls))
]