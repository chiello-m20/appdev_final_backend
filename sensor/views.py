from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SensorDataSerializer
from .models import SensorData

@api_view(['GET', 'POST'])
def receive_data(request):
    if request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data received and saved."})
        return Response(serializer.errors, status=400)

    elif request.method == 'GET':
        data = SensorData.objects.all().order_by('-timestamp')
        serializer = SensorDataSerializer(data, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def clear_sensor_data(request):
    SensorData.objects.all().delete()
    return Response({"message": "All sensor data cleared."})
