from rest_framework import serializers

from measurement.models import Measurement, Sensor


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class MeasurementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']