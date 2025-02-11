# Generated by Django 5.1.6 on 2025-02-09 13:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_specification_doctor_specialization_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-date', 'start_time']},
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_id',
            field=models.CharField(default=1, editable=False, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='doctoravailability',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='accounts.doctor'),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('doctor', 'date', 'start_time')},
        ),
    ]
