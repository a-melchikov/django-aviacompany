# Generated by Django 5.0.6 on 2024-06-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crew', '0002_rename_position_crewmember_name_and_more'),
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crewmember',
            name='flights',
            field=models.ManyToManyField(related_name='crew_members', to='flights.flight'),
        ),
    ]
