# Generated by Django 3.2.5 on 2021-07-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='discription',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
