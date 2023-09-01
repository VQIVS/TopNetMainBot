from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LinkSerializer
from ...models import Link

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == "GET":
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        data = serializer.data
        return Response(data)
    elif request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Link saved successfully")  # Add this line for debugging
            return Response(serializer.data)
        else:
            print("Serializer errors:", serializer.errors)  # Add this line for debugging
            return Response(serializer.errors)
