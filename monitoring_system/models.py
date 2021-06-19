import datetime
import uuid

from django.db import models


class Doctor(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    first_name = models.CharField(null=True, max_length=255)
    last_name = models.CharField(null=True, max_length=255)
    department = models.CharField(null=True, max_length=255)

    class Meta:
        db_table = 'doctors'


class RegistryAddress(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    region = models.CharField(null=True, max_length=255)
    city = models.CharField(null=True, max_length=255)
    street = models.CharField(null=True, max_length=255)
    house = models.CharField(null=True, max_length=255)
    apartment = models.CharField(null=True, max_length=255)

    class Meta:
        db_table = 'registry_address'


class Patient(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    first_name = models.CharField(null=True, max_length=255)
    last_name = models.CharField(null=True, max_length=255)
    patronymic = models.CharField(null=True, max_length=255)
    sex = models.BooleanField(null=True)  # female = true, male = false
    date_of_birth = models.DateField(null=True)
    registry_address_id = models.CharField(null=True, max_length=255)
    phone_number = models.CharField(null=True, max_length=255)
    email = models.EmailField(null=True, max_length=255)
    oms = models.CharField(null=True, max_length=255)
    insurance = models.CharField(null=True, max_length=255)
    passport = models.CharField(null=True, max_length=255)
    doctor_id = models.CharField(null=True, max_length=255)
    age = models.CharField(null=True, max_length=150)

    class Meta:
        db_table = 'patients'


class Measurement(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    date = models.DateField(null=True)
    upper_point = models.IntegerField(null=True)
    lower_point = models.IntegerField(null=True)
    pulse = models.IntegerField(null=True)
    patient_id = models.CharField(null=True, max_length=255)

    class Meta:
        db_table = 'measurements'


class AuthDoctor(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    login = models.CharField(null=True, max_length=255)
    password = models.CharField(null=True, max_length=255)

    class Meta:
        db_table = 'auth_doctors'
