# Generated by Django 2.0.2 on 2018-08-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20180827_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
