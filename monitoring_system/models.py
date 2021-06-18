import datetime
import uuid

from django.db import models


class Doctor(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    name = models.CharField(null=True,max_length=255)
    department = models.CharField(null=True,max_length=255)

    class Meta:
        db_table = 'doctors'


class RegistryAddress(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    region = models.CharField(null=True,max_length=255)
    city = models.CharField(null=True,max_length=255)
    street = models.CharField(null=True,max_length=255)
    house = models.CharField(null=True,max_length=255)
    apartment = models.CharField(null=True,max_length=255)

    class Meta:
        db_table = 'registry_address'


class Patient(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    sex = models.BooleanField(null=True)  # female = true, male = false
    date_of_birth = models.DateField(null=True)
    registry_address = models.ForeignKey(RegistryAddress, null=True, on_delete=models.PROTECT)
    phone = models.CharField(null=True,max_length=255)
    oms = models.CharField(null=True,max_length=255)
    insurance = models.CharField(null=True,max_length=255)
    passport = models.CharField(null=True,max_length=255)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'patients'


class Measurement(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    date = models.DateField(null=True)
    upper_point = models.IntegerField(null=True)
    lower_point = models.IntegerField(null=True)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'measurements'
