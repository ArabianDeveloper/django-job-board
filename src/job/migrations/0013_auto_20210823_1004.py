# Generated by Django 3.2.5 on 2021-08-23 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_job_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='image',
            field=models.ImageField(default='', upload_to='Applays/images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='job.category'),
        ),
    ]