from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ..models import InformatieObjectType, ZaakInformatieobjectType
from .mixins import ConceptAdminMixin, GeldigheidAdminMixin


class ZaakInformatieobjectTypeInline(admin.TabularInline):
    model = ZaakInformatieobjectType
    extra = 1
    raw_id_fields = ("zaaktype", "statustype")


@admin.register(InformatieObjectType)
class InformatieObjectTypeAdmin(
    GeldigheidAdminMixin, ConceptAdminMixin, admin.ModelAdmin
):
    list_display = ("catalogus", "omschrijving", "informatieobjectcategorie")
    list_filter = ("catalogus", "informatieobjectcategorie")
    search_fields = (
        "omschrijving",
        "informatieobjectcategorie",
        "trefwoord",
        "toelichting",
    )
    ordering = ("catalogus", "omschrijving")

    # Details
    fieldsets = (
        (
            _("Algemeen"),
            {
                "fields": (
                    "omschrijving",
                    "informatieobjectcategorie",
                    "trefwoord",
                    "vertrouwelijkheidaanduiding",
                    "model",
                    "toelichting",
                )
            },
        ),
        (_("Relaties"), {"fields": ("catalogus", "omschrijving_generiek")}),
    )
    inlines = (ZaakInformatieobjectTypeInline,)  # zaaktypes
