# Generated by Django 3.2.4 on 2021-06-15 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_alter_schedule_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='type',
            new_name='work_type',
        ),
    ]
