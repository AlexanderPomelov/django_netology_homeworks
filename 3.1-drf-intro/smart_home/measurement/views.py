
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, \
    CreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import (SensorDetailSerializer, SensorListSerializer,
                                                MeasurementListSerializer)


class SensorsAPIView(ListCreateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorDetailAPIView(RetrieveUpdateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementAPIView(CreateAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementListSerializer




