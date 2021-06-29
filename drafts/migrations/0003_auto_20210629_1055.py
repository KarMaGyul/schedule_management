# Generated by Django 3.2.4 on 2021-06-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0002_auto_20210614_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='approval_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draft',
            name='draft_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='draft',
            name='end_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draft',
            name='start_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draft',
            name='type',
            field=models.CharField(choices=[('연차', '휴가'), ('반차', '휴가'), ('공가', '휴가'), ('경조', '휴가'), ('시차출퇴근제', '근무제도'), ('선택근무제', '근무제도'), ('재량근무제', '근무제도'), ('재택근무제', '근무제도')], max_length=64),
        ),
    ]