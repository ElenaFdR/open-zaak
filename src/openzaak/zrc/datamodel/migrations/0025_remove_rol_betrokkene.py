# Generated by Django 2.0.6 on 2018-07-25 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0024_zaakobject_object_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='betrokkene',
        ),
    ]
