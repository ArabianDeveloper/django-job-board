# Generated by Django 3.2.5 on 2021-08-27 13:04

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_testimonial_image'),
        ('job', '0017_auto_20210827_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='home.top_companies'),
        ),
    ]
