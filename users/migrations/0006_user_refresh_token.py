# Generated by Django 3.2.4 on 2021-06-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_employee_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]
