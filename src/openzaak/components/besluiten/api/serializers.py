"""
Serializers of the Besluit Registratie Component REST API
"""
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from vng_api_common.serializers import add_choice_values_help_text
from vng_api_common.utils import get_help_text
from vng_api_common.validators import IsImmutableValidator, validate_rsin

from openzaak.components.catalogi.models import BesluitType
from openzaak.components.documenten.api.serializers import (
    EnkelvoudigInformatieObjectHyperlinkedRelatedField,
)
from openzaak.components.documenten.models import EnkelvoudigInformatieObject
from openzaak.components.zaken.models import Zaak
from openzaak.utils.serializer_fields import LengthHyperlinkedRelatedField

from ..constants import VervalRedenen
from ..models import Besluit, BesluitInformatieObject
from .validators import (
    BesluittypeZaaktypeValidator,
    UniekeIdentificatieValidator,
    ZaaktypeInformatieobjecttypeRelationValidator,
)


class BesluitSerializer(serializers.HyperlinkedModelSerializer):
    besluittype = LengthHyperlinkedRelatedField(
        view_name="besluittype-detail",
        lookup_field="uuid",
        queryset=BesluitType.objects,
        max_length=200,
        min_length=1,
        help_text=get_help_text("besluiten.Besluit", "besluittype"),
    )
    zaak = LengthHyperlinkedRelatedField(
        view_name="zaak-detail",
        lookup_field="uuid",
        queryset=Zaak.objects,
        required=False,
        allow_null=True,
        max_length=200,
        help_text=get_help_text("besluiten.Besluit", "zaak"),
    )
    vervalreden_weergave = serializers.CharField(
        source="get_vervalreden_display", read_only=True
    )

    class Meta:
        model = Besluit
        fields = (
            "url",
            "identificatie",
            "verantwoordelijke_organisatie",
            "besluittype",
            "zaak",
            "datum",
            "toelichting",
            "bestuursorgaan",
            "ingangsdatum",
            "vervaldatum",
            "vervalreden",
            "vervalreden_weergave",
            "publicatiedatum",
            "verzenddatum",
            "uiterlijke_reactiedatum",
        )
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
            "identificatie": {"validators": [IsImmutableValidator()]},
            "verantwoordelijke_organisatie": {
                "validators": [IsImmutableValidator(), validate_rsin]
            },
        }
        validators = [UniekeIdentificatieValidator(), BesluittypeZaaktypeValidator()]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        value_display_mapping = add_choice_values_help_text(VervalRedenen)
        self.fields["vervalreden"].help_text += f"\n\n{value_display_mapping}"


class BesluitInformatieObjectSerializer(serializers.HyperlinkedModelSerializer):
    informatieobject = EnkelvoudigInformatieObjectHyperlinkedRelatedField(
        view_name="enkelvoudiginformatieobject-detail",
        lookup_field="uuid",
        queryset=EnkelvoudigInformatieObject.objects,
        help_text="URL-referentie naar het INFORMATIEOBJECT (in de Documenten "
        "API) waarin (een deel van) het besluit beschreven is.",
        max_length=1000,
        min_length=1,
        validators=[IsImmutableValidator()],
    )

    class Meta:
        model = BesluitInformatieObject
        fields = ("url", "informatieobject", "besluit")
        validators = [
            UniqueTogetherValidator(
                queryset=BesluitInformatieObject.objects.all(),
                fields=["besluit", "informatieobject"],
            ),
            ZaaktypeInformatieobjecttypeRelationValidator(),
        ]
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
            "besluit": {"lookup_field": "uuid", "validators": [IsImmutableValidator()]},
        }
