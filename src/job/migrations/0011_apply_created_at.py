# Generated by Django 3.2.5 on 2021-07-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
