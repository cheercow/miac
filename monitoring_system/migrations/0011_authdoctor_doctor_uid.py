# Generated by Django 3.2.4 on 2021-06-19 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0010_alter_measurement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='authdoctor',
            name='doctor_uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='monitoring_system.doctor'),
        ),
    ]
