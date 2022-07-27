# Generated by Django 3.2.5 on 2021-08-27 13:34

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=django_countries.fields.CountryField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
