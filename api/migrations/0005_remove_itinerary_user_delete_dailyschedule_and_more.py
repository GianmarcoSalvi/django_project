# Generated by Django 4.1.7 on 2023-02-26 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_itinerary_dailyschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='user',
        ),
        migrations.DeleteModel(
            name='DailySchedule',
        ),
        migrations.DeleteModel(
            name='Itinerary',
        ),
    ]
