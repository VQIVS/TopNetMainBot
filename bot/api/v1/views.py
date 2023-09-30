from .serializers import LinkSerializer, UserSerializer, OrderSerializer, EmailSerializer
from ...models import Link, User, Order, Email
from rest_framework.viewsets import ModelViewSet


class ModelViewSetLinks(ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

class ModelViewSetUser(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ModelViewSetOrder(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ModelViewSetEmail(ModelViewSet):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()










