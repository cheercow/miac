# Generated by Django 3.2.4 on 2021-06-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0005_auto_20210618_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='patient',
        ),
        migrations.AddField(
            model_name='measurement',
            name='patient_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
