import uuid

from rest_framework.views import APIView, Response

from monitoring_system.models import Patient, Measurement
from monitoring_system.serializers import PatientSerializer, MeasurementSerializer


class PatientView(APIView):
    def get(self, request, uid):
        patient = Patient.objects.get(uid=uid)
        patient_data = PatientSerializer(patient).data
        return Response(status=200, data=patient_data)


class PatientListView(APIView):
    def get(self, request):
        patients = []
        patient_list = Patient.objects.all()
        for patient in patient_list:
            patient_data = PatientSerializer(patient).data
            patients.append(patient_data)
        return Response(status=200, data=patients)


class PatientMeasurementsView(APIView):
    def get(self, request, uid):
        measurements = []
        patient = Patient.objects.get(uid=uid)
        measurement_list = Measurement.objects.filter(patient_id=patient.id)
        for measurement in measurement_list:
            measurement_data = MeasurementSerializer(measurement).data
            measurements.append(measurement_data)
        return Response(status=200, data=measurements)

    def post(self, request, uid):
        pass
        data = request.data
        patient = Patient.objects.get(uid=uid)
        measurement = Measurement.objects.create(uid=uuid.uuid4(),
                                                 date=data['date'],
                                                 upper_point=data['upper_point'],
                                                 lower_point=data['lower_point'],
                                                 patient_id=patient.id)
        measurement_data = MeasurementSerializer(measurement).data
        return Response(status=201, data=measurement_data)


