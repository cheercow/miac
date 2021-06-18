import datetime
import uuid

from django.db import models


class RegistryAddress(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    region = models.CharField(null=True)
    city = models.CharField(null=True)
    street = models.CharField(null=True)
    house = models.CharField(null=True)
    apartment = models.CharField(null=True)

    class Meta:
        db_table = 'registry_address'


class Patient(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField(null=True, default=datetime.datetime.now())
    end_date = models.DecimalField(null=True)
    sex = models.BooleanField(null=True)  # female = true, male = false
    date_of_birth = models.DateField(null=True)
    registry_address = models.ForeignKey(RegistryAddress, null=True, on_delete=models.PROTECT)
    phone = models.CharField(null=True)
    oms = models.CharField(null=True)
    insurance = models.CharField(null=True)
    passport = models.CharField(null=True)

    class Meta:
        db_table = 'patients'


class Measurement(models.Model):
    uid = models.UUIDField(default=uuid.UUID, null=False, db_index=True)
    date = models.DateField(null=True, default=datetime.datetime.now())
    upper_point = models.IntegerField(null=True)
    lower_point = models.IntegerField(null=True)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'measurements'
