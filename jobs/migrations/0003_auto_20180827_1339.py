# Generated by Django 2.0.2 on 2018-08-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
