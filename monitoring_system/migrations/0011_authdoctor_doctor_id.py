# Generated by Django 3.2.4 on 2021-06-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0010_alter_measurement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='authdoctor',
            name='doctor_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]