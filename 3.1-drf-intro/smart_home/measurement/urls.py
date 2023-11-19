from django.urls import path

from measurement.views import SensorsAPIView, SensorDetailAPIView, MeasurementAPIView

urlpatterns = [
    path('sensors/', SensorsAPIView.as_view()),
    path('sensors/<pk>/', SensorDetailAPIView.as_view()),
    path('measurements/', MeasurementAPIView.as_view()),

]
