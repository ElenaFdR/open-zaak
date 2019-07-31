# Generated by Django 2.0.6 on 2018-07-24 09:41

import uuid

from django.db import migrations


def gen_uuid(apps, schema_editor):
    Zaak = apps.get_model('datamodel', 'Zaak')
    Status = apps.get_model('datamodel', 'Status')
    Rol = apps.get_model('datamodel', 'Rol')
    ZaakObject = apps.get_model('datamodel', 'ZaakObject')
    ZaakEigenschap = apps.get_model('datamodel', 'ZaakEigenschap')
    KlantContact = apps.get_model('datamodel', 'KlantContact')
    OrganisatorischeEenheid = apps.get_model('datamodel', 'OrganisatorischeEenheid')

    for Model in (Zaak, Status, Rol, ZaakObject, ZaakEigenschap, KlantContact, OrganisatorischeEenheid):
        for row in Model.objects.all():
            row.uuid = uuid.uuid4()
            row.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0019_auto_20180724_0941'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, migrations.RunPython.noop),
    ]
