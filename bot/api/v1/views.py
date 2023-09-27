from .serializers import LinkSerializer, UserSerializer
from ...models import Link, User
from rest_framework.viewsets import ModelViewSet


class ModelViewSetLinks(ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

class ModelViewSetUser(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()






