# Generated by Django 2.2.2 on 2019-08-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besluiten', '0003_auto_20190807_1021'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='besluit',
            name='fk_or_url_filled',
        ),
        migrations.RemoveConstraint(
            model_name='besluit',
            name='fk_or_url_filled_zaak',
        ),
        migrations.RemoveConstraint(
            model_name='besluitinformatieobject',
            name='fk_or_url_filled',
        ),
        migrations.AlterField(
            model_name='besluitinformatieobject',
            name='informatieobject_remote',
            field=models.URLField(blank=True, default=None, max_length=1000),
        ),
        migrations.AddConstraint(
            model_name='besluit',
            constraint=models.CheckConstraint(check=models.Q(models.Q(models.Q(_negated=True, besluittype_local__isnull=True), ('besluittype_remote', '')), models.Q(('besluittype_local__isnull', True), models.Q(_negated=True, besluittype_remote='')), _connector='OR'), name='besluittype_local_or_besluittype_remote_filled'),
        ),
        migrations.AddConstraint(
            model_name='besluit',
            constraint=models.CheckConstraint(check=models.Q(models.Q(models.Q(_negated=True, zaak_local__isnull=True), ('zaak_remote', '')), models.Q(('zaak_local__isnull', True), models.Q(_negated=True, zaak_remote='')), _connector='OR'), name='zaak_local_or_zaak_remote_filled'),
        ),
        migrations.AddConstraint(
            model_name='besluitinformatieobject',
            constraint=models.UniqueConstraint(condition=models.Q(_negated=True, informatieobject_remote=''), fields=('besluit', 'informatieobject_remote'), name='unique_informatieobject_remote'),
        ),
        migrations.AddConstraint(
            model_name='besluitinformatieobject',
            constraint=models.UniqueConstraint(fields=('besluit', 'informatieobject_local'), name='unique_informatieobject_local'),
        ),
        migrations.AddConstraint(
            model_name='besluitinformatieobject',
            constraint=models.CheckConstraint(check=models.Q(models.Q(models.Q(_negated=True, informatieobject_local__isnull=True), ('informatieobject_remote', '')), models.Q(('informatieobject_local__isnull', True), models.Q(_negated=True, informatieobject_remote='')), _connector='OR'), name='informatieobject_local_or_informatieobject_remote_filled'),
        ),
    ]