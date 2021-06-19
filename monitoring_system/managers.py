import uuid

from monitoring_system.models import AuthDoctor, Doctor, Medicine, Patient, Prescription


class PrescriptionManager:

    def set_prescription(self, request, uid):
        self.request_data = request.data
        model_info = self.get_model_info(uid)
        self.model_prec = Prescription(**self.request_data)

    def get_prescription(self, request, uid):
        instance = Prescription.objects.get(patient_id=uid)
        model_info = {
            'type': instance.type,
            'title': instance.title,
            'description': instance.description,
            'date_from': instance.date_from,
            'date_to': instance.date_to,
            'patient_id': uid,
        }
        return model_info

    def get_model_info(self, uid):
        model_info = {
            'type': self.request_data.get('type'),
            'title': self.request_data.get('title'),
            'description': self.request_data.get('description'),
            'date_from': self.request_data.get('date_from'),
            'date_to': self.request_data.get('date_to'),
            'patient_id': uid,
        }
        return model_info


class MedicineManager:
    def set_meds(self, request, uid):
        self.patient = Patient.objects.get(uid=uid)
        self.medicine = Medicine.objects.create(patient_id=self.patient.id, name=request.data.get('medicine'))

    def get_meds(self, request, uid):
        self.patient = Patient.objects.get(uid=uid)
        self.queryset = Medicine.objects.filter(patient_id=self.patient.id)
        list_of_meds = []
        for element in self.queryset:
            list_of_meds.append(element.name)
        return list_of_meds


class DoctorAuthManager:
    def __init__(self, request):
        self.model_auth = AuthDoctor
        self.model_doctor = Doctor
        self.request_data = request.data

    def registry_doc(self):
        self.login = self.request_data.get('login')
        self.password = self.request_data.get('password')

        self.first_name = self.request_data.get('first_name')
        self.last_name = self.request_data.get('last_name')
        self.department = self.request_data.get('department')
        doc_instance = self.model_doctor.objects.create(uid=uuid.uuid4(), first_name=self.first_name,
                                                        last_name=self.last_name,
                                                        department=self.department)
        auth_instance = self.model_auth.objects.create(uid=uuid.uuid4(), login=self.login, password=self.password,
                                                       doctor_id=doc_instance.id)

        return doc_instance.uid

    def auth_check(self):
        self.login = self.request_data.get('login')
        self.password = self.request_data.get('password')
        if self.model_auth.objects.get(login=self.login, password=self.password):
            auth_instance = self.model_auth.objects.get(login=self.login, password=self.password)
            doctor = Doctor.objects.get(id=auth_instance.doctor_id)
            return doctor.uid
