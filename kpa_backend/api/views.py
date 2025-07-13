from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import KPAForm
from .serializers import KPAFormSerializer

@api_view(['POST'])
def create_kpa_form(request):
    serializer = KPAFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_kpa_form(request, pk):
    try:
        form = KPAForm.objects.get(pk=pk)
    except KPAForm.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = KPAFormSerializer(form)
    return Response(serializer.data)
