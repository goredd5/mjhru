# Generated by Django 2.0.2 on 2018-08-10 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='details',
        ),
    ]
