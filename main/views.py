from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GridSerializer


@api_view(['POST'])
def calculate_closest_points(request):
    serializer = GridSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        obj = serializer.save()
    return Response({'closest_points': obj.closest_points})
