# Generated by Django 3.2.5 on 2021-08-23 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_testimonial_image'),
        ('job', '0015_rename_j_category_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.top_companies'),
            preserve_default=False,
        ),
    ]
