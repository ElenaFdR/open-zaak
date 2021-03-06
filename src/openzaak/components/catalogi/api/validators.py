from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from rest_framework.serializers import ValidationError
from vng_api_common.constants import (
    BrondatumArchiefprocedureAfleidingswijze as Afleidingswijze,
)

from openzaak.client import fetch_object

from ..constants import SelectielijstKlasseProcestermijn as Procestermijn
from ..models import ZaakType


class ZaaktypeGeldigheidValidator:
    """
    Validate that the (new) object is unique between a start and end date.

    Empty end date is an open interval, which means that the object cannot
    be created after the start date.
    """

    message = _(
        "Dit zaaktype komt al voor binnen de catalogus en opgegeven geldigheidsperiode."
    )
    code = "overlap"

    def set_context(self, serializer):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # Determine the existing instance, if this is an update operation.
        self.instance = getattr(serializer, "instance", None)

    def __call__(self, attrs):
        catalogus = attrs["catalogus"]
        zaaktype_omschrijving = attrs["zaaktype_omschrijving"]
        datum_begin_geldigheid = attrs["datum_begin_geldigheid"]
        datum_einde_geldigheid = attrs.get("datum_einde_geldigheid")

        query = ZaakType.objects.filter(
            Q(catalogus=catalogus),
            Q(zaaktype_omschrijving=zaaktype_omschrijving),
            Q(datum_einde_geldigheid=None)
            | Q(datum_einde_geldigheid__gte=datum_begin_geldigheid),  # noqa
        )
        if datum_einde_geldigheid is not None:
            query = query.filter(datum_begin_geldigheid__lte=datum_einde_geldigheid)

        if self.instance:
            query = query.exclude(pk=self.instance.pk)

        # regel voor zaaktype omschrijving
        if query.exists():
            raise ValidationError({"begin_geldigheid": self.message}, code=self.code)


class RelationCatalogValidator:
    code = "relations-incorrect-catalogus"
    message = _("The {} has catalogus different from created object")

    def __init__(self, relation_field: str, catalogus_field="catalogus"):
        self.relation_field = relation_field
        self.catalogus_field = catalogus_field

    def __call__(self, attrs: dict):
        relations = attrs.get(self.relation_field)
        catalogus = attrs.get(self.catalogus_field)

        if not relations:
            return

        if not isinstance(relations, list):
            relations = [relations]

        for relation in relations:
            if relation.catalogus != catalogus:
                raise ValidationError(
                    self.message.format(self.relation_field), code=self.code
                )


class ProcesTypeValidator:
    code = "procestype-mismatch"
    message = _("{} should belong to the same procestype as {}")

    def __init__(self, relation_field: str, zaaktype_field="zaaktype"):
        self.relation_field = relation_field
        self.zaaktype_field = zaaktype_field

    def __call__(self, attrs: dict):
        selectielijstklasse_url = attrs.get(self.relation_field)
        zaaktype = attrs.get(self.zaaktype_field)

        if not selectielijstklasse_url:
            return

        selectielijstklasse = fetch_object("resultaat", selectielijstklasse_url)

        if selectielijstklasse["procesType"] != zaaktype.selectielijst_procestype:
            raise ValidationError(
                self.message.format(self.relation_field, self.zaaktype_field),
                code=self.code,
            )


class ProcestermijnAfleidingswijzeValidator:
    code = "invalid-afleidingswijze-for-procestermijn"
    message = _(
        "afleidingswijze cannot be {} when selectielijstklasse.procestermijn is {}"
    )

    def __init__(
        self,
        selectielijstklasse_field: str,
        archiefprocedure_field="brondatum_archiefprocedure",
    ):
        self.selectielijstklasse_field = selectielijstklasse_field
        self.archiefprocedure_field = archiefprocedure_field

    def __call__(self, attrs: dict):
        selectielijstklasse_url = attrs.get(self.selectielijstklasse_field)
        archiefprocedure = attrs.get(self.archiefprocedure_field)

        if not selectielijstklasse_url:
            return

        selectielijstklasse = fetch_object("resultaat", selectielijstklasse_url)
        procestermijn = selectielijstklasse["procestermijn"]
        afleidingswijze = archiefprocedure["afleidingswijze"]

        error = False
        if (
            procestermijn == Procestermijn.nihil
            and afleidingswijze != Afleidingswijze.afgehandeld
        ):
            error = True
        elif (
            procestermijn == Procestermijn.ingeschatte_bestaansduur_procesobject
            and afleidingswijze != Afleidingswijze.termijn
        ):
            error = True

        if error:
            raise ValidationError(
                self.message.format(afleidingswijze, procestermijn), code=self.code
            )
