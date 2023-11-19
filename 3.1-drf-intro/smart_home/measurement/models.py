from django.db import models

class Sensor(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

class Measurement(models.Model):

    id = models.IntegerField(primary_key=True)
    temperature = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )