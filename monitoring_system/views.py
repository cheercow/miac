import uuid

from rest_framework.views import APIView, Response

from monitoring_system.managers import DoctorAuthManager, MedicineManager, PrescriptionManager
from monitoring_system.models import Patient, Measurement, Doctor
from monitoring_system.serializers import PatientSerializer, MeasurementSerializer, DoctorSerializer


class PatientView(APIView):
    def get(self, request, uid):
        patient = Patient.objects.get(uid=uid)
        patient_data = PatientSerializer(patient).data
        return Response(status=200, data=patient_data)


class DoctorView(APIView):
    def get(self, request, uid):
        doctor = Doctor.objects.get(uid=uid)
        doctor_data = DoctorSerializer(doctor).data
        return Response(status=200, data=doctor_data)


class PatientListView(APIView):
    def get(self, request):
        patients = []
        patient_list = Patient.objects.all()
        for patient in patient_list:
            patient_data = PatientSerializer(patient).data
            patients.append(patient_data)
        return Response(status=200, data=patients)


class PrivatePatientListView(APIView):
    def get(self, request):
        doctor_uid = request.headers['X-AUTH']
        doctor = Doctor.objects.get(uid=doctor_uid)
        patients = []
        patient_list = Patient.objects.filter(doctor_id=doctor.id)
        for patient in patient_list:
            patient_data = PatientSerializer(patient).data
            patients.append(patient_data)
        return Response(status=200, data=patients)


class PrivatePatientView(APIView):
    def post(self, request, uid):
        doctor_uid = request.headers['X-AUTH']
        doctor = Doctor.objects.get(uid=doctor_uid)
        patient = Patient.objects.get(uid=uid)
        patient.doctor_id = doctor.id
        patient.save()
        return Response(status=200)

    def delete(self, request, uid):
        patient = Patient.objects.get(uid=uid)
        patient.doctor_id = None
        patient.save()
        return Response(status=200)


class SearchPatientView(APIView):
    def get(self, request, term):
        patients = []
        patient_list = Patient.objects.filter(first_name=term.split[0], last_name=term.split[1])
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
        data = request.data
        patient = Patient.objects.get(uid=uid)
        measurement = Measurement.objects.create(uid=uuid.uuid4(),
                                                 upper_point=data['upper_point'],
                                                 lower_point=data['lower_point'],
                                                 pulse=data['pulse'],
                                                 patient_id=patient.id)
        measurement_data = MeasurementSerializer(measurement).data
        return Response(status=201, data=measurement_data)


class DoctorRegistryView(APIView):
    def post(self, request):
        manager = DoctorAuthManager(request)
        user_uid = manager.registry_doc()
        return Response(status=200, data=user_uid)


class DoctorAuthView(APIView):
    def post(self, request):
        manager = DoctorAuthManager(request)
        user_uid = manager.auth_check()
        return Response(status=200, data=user_uid)


class PatientAuthView(APIView):
    def post(self, request):
        data = request.data
        patient = Patient.objects.get(snils=data['snils'])
        return Response(status=200, data=patient.uid)


class MedicinehView(APIView):

    def post(self, request, uid):
        MedicineManager().set_meds(request, uid)
        return Response(status=200)

    def get(self, request, uid):
        meds = MedicineManager().get_meds(request, uid)
        return Response(status=200, data=meds)


class PrescriptionView(APIView):
    def post(self, request, uid):
        instance = PrescriptionManager().set_prescription(request, uid)
        return Response(status=200,data=instance)

    def get(self, request, uid):
        info = PrescriptionManager().get_prescription(request, uid)
        return Response(status=200, data=info)

    def put(self, request, uid):
        instance = PrescriptionManager().put_prescription(request, uid)
        return Response(status=200,data=instance)
