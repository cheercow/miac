import uuid

from monitoring_system.models import AuthDoctor, Doctor, Medicine


class MedicineManager:
    def __init__(self):
        self.model = Medicine

    def get_meds(self):
        return self.model.objects.all()

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
                                                       doctor_uid=doc_instance.uid)

        return doc_instance.uid

    def auth_check(self):
        self.login = self.request_data.get('login')
        self.password = self.request_data.get('password')
        if self.model_auth.objects.get(login=self.login, password=self.password):
            auth_instance = self.model_auth.objects.get(login=self.login, password=self.password)
            return auth_instance.doctor_uid
