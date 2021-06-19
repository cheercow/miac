# Generated by Django 3.2.4 on 2021-06-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='start_date',
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
