from rest_framework import serializers

from monitoring_system.models import Patient, Measurement, Doctor


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ("id",)
        depth = 1


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ("id",)
        depth = 1


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        exclude = ("id",)
        depth = 1