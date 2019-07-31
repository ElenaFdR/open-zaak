# Generated by Django 2.2.2 on 2019-07-29 10:14

from django.db import migrations

from vng_api_common.db.operations import UpdateChoiceValues

from ..constants import (
    GeslachtsAanduiding, SoortRechtsvorm, TyperingInrichtingselement,
    TyperingKunstwerk, TyperingWater
)


class GeslachtsAanduidingUpdate(UpdateChoiceValues):
    mapping = {
        "M": GeslachtsAanduiding.man,
        "V": GeslachtsAanduiding.vrouw,
        "O": GeslachtsAanduiding.onbekend,
    }


class SoortRechtsvormUpdate(UpdateChoiceValues):
    mapping = {
        "Besloten Vennootschap": SoortRechtsvorm.besloten_vennootschap,
        "Cooperatie, Europees Economische Samenwerking": SoortRechtsvorm.cooperatie_europees_economische_samenwerking,
        "Europese Cooperatieve Venootschap": SoortRechtsvorm.europese_cooperatieve_vennootschap,
        "Europese Naamloze Vennootschap": SoortRechtsvorm.europese_naamloze_vennootschap,
        "Kerkelijke Organisatie": SoortRechtsvorm.kerkelijke_organisatie,
        "Naamloze Vennootschap": SoortRechtsvorm.naamloze_vennootschap,
        "Onderlinge Waarborg Maatschappij": SoortRechtsvorm.onderlinge_waarborg_maatschappij,
        "Overig privaatrechtelijke rechtspersoon": SoortRechtsvorm.overig_privaatrechtelijke_rechtspersoon,
        "Stichting": SoortRechtsvorm.stichting,
        "Vereniging": SoortRechtsvorm.vereniging,
        "Vereniging van Eigenaars": SoortRechtsvorm.vereniging_van_eigenaars,
        "Publiekrechtelijke Rechtspersoon": SoortRechtsvorm.publiekrechtelijke_rechtspersoon,
        "Vennootschap onder Firma": SoortRechtsvorm.vennootschap_onder_firma,
        "Maatschap": SoortRechtsvorm.maatschap,
        "Rederij": SoortRechtsvorm.rederij,
        "Commanditaire vennootschap": SoortRechtsvorm.commanditaire_vennootschap,
        "Kapitaalvennootschap binnen EER": SoortRechtsvorm.kapitaalvennootschap_binnen_eer,
        "Overige buitenlandse rechtspersoon vennootschap": SoortRechtsvorm.overige_buitenlandse_rechtspersoon_vennootschap,  # noqa
        "Kapitaalvennootschap buiten EER": SoortRechtsvorm.kapitaalvennootschap_buiten_eer,
    }


class TyperingInrichtingselementUpdate(UpdateChoiceValues):
    mapping = {
        "Bak": TyperingInrichtingselement.bak,
        "Bord": TyperingInrichtingselement.bord,
        "Installatie": TyperingInrichtingselement.installatie,
        "Kast": TyperingInrichtingselement.kast,
        "Mast": TyperingInrichtingselement.mast,
        "Paal": TyperingInrichtingselement.paal,
        "Sensor": TyperingInrichtingselement.sensor,
        "Straatmeubilair": TyperingInrichtingselement.straatmeubilair,
        "Waterinrichtingselement": TyperingInrichtingselement.waterinrichtingselement,
        "Weginrichtingselement": TyperingInrichtingselement.weginrichtingselement,
    }


class TyperingKunstwerkUpdate(UpdateChoiceValues):
    mapping = {
        "Keermuur": TyperingKunstwerk.keermuur,
        "Overkluizing": TyperingKunstwerk.overkluizing,
        "Duiker": TyperingKunstwerk.duiker,
        "Faunavoorziening": TyperingKunstwerk.faunavoorziening,
        "Vispassage": TyperingKunstwerk.vispassage,
        "Bodemval": TyperingKunstwerk.bodemval,
        "Coupure": TyperingKunstwerk.coupure,
        "Ponton": TyperingKunstwerk.ponton,
        "Voorde": TyperingKunstwerk.voorde,
        "Hoogspanningsmast": TyperingKunstwerk.hoogspanningsmast,
        "Gemaal": TyperingKunstwerk.gemaal,
        "Perron": TyperingKunstwerk.perron,
        "Sluis": TyperingKunstwerk.sluis,
        "Strekdam": TyperingKunstwerk.strekdam,
        "Steiger": TyperingKunstwerk.steiger,
        "Stuw": TyperingKunstwerk.stuw,
    }


class TyperingWaterUpdate(UpdateChoiceValues):
    mapping = {
        "Zee": TyperingWater.zee,
        "Waterloop": TyperingWater.waterloop,
        "Watervlakte": TyperingWater.watervlakte,
        "Greppel, droge sloot": TyperingWater.greppel_droge_sloot,
    }


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0081_auto_20190729_1013'),
    ]

    operations = [
        GeslachtsAanduidingUpdate("datamodel.NatuurlijkPersoon", "geslachtsaanduiding"),
        SoortRechtsvormUpdate("datamodel.NietNatuurlijkPersoon", "inn_rechtsvorm"),
        TyperingInrichtingselementUpdate("datamodel.Inrichtingselement", "type"),
        TyperingKunstwerkUpdate("datamodel.Kunstwerkdeel", "type"),
        TyperingWaterUpdate("datamodel.Waterdeel", "type_waterdeel"),
    ]
