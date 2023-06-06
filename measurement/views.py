# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .models import Measurment, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer
from rest_framework.response import Response


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
    def post(self, request):
        sensor = Sensor(name=request.data.get('name'), description=request.data.get('description')).save()
        return Response(f'Сенсор добавлен,{sensor.name}')
    
class SensorDetail(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()
    
    def patch(self, request, *args, **kwargs):
        Sensor.objects.filter(id=kwargs.get('pk')).update(description=request.data.get('description'))
        return Response(f'Измененеия внесены')

class MeasureView(ListAPIView):
    queryset = Measurment.objects.all()
    serializer_class = MeasurementSerializer
    
    def post(self, request):
        measure = Measurment(sensor_id=request.data.get('sensor'), temperature=request.data.get('temperature')).save()
        return Response(f'Измерения добавлены')

class MeasureDetail(RetrieveUpdateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurment.objects.all()