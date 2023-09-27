from django.urls import path, include
from .views import ModelViewSetLinks, ModelViewSetUser
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('links', ModelViewSetLinks, basename="links-api")
router.register('User', ModelViewSetUser, basename="Users-api")
app_name = "api-v1"

urlpatterns = [
    # path('post_list/', post_list, name='post_list')
    path('', include(router.urls))
]