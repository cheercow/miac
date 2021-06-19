from rest_framework import serializers

from monitoring_system.models import Patient, Measurement


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ("id",)
        depth = 1


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        exclude = ("id",)
        depth = 1