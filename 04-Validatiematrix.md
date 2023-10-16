
# De validatiematrix

De volgende versie van de standaarden zijn gebruikt voor het samenstellen van de validatiematrix:
- Informatiemodel Omgevingswet (IMOW) Versie 2.0.2.
- STOP standaard Versie 1.3.0.
- Ook worden validatieregels van OZON en het LVBB bronhouderskoppelvlak opgenomen.

Betekenis van de kolommen:

| Kolom         | Omschrijving |
|---------------|--------------|
| identificatie | Unieke identificatie van de validatieregel die gebruikt kan worden in communicatie over de regel. |
| ernst         | 'Blokkerend' of 'Waarschuwing'. Blokkerende regels leiden tot afkeuring van het document in de keten. Een waarschuwing resulteert niet tot afkeuring van het document maar levert een melding bij de indiener van het document. |
| omschrijving  | Eenduidige omschrijving van de validatieregel. |


De validatiematrix bevat de volgende validatieregels:

| Identificatie | Ernst | Omschrijving|
|:--------------|:------|:------------|
|BHKV1004|Blokkerend|Voor een ontwerpbesluit MAG GEEN tijdstempel worden meegeleverd.|
|BHKV1005|Blokkerend|Een Besluit (tekst:BesluitCompact of tekst:BesluitKlassiek) MOET een identificatie hebben die aangeeft dat het een Besluit betreft (data:soortWork = /join/id/stop/work_003).|
|LVBB1032|Blokkerend|Een aangeleverd manifest-ow.xml (of bij een interne opdracht aangeleverd manifest-bhkv.xml) moet voldoen aan de eisen van het schema van de STOP-standaard.|
|LVBB1506|Blokkerend|Het publicatiebestand, waarvan de naam in de opdracht is vermeld, moet aanwezig zijn.|
|LVBB4200|Blokkerend|De 'datum JWV' van een wordt-versie MOET later zijn dan de 'datum JWV' van de was-versie.|
|LVBB4201|Blokkerend|Indien de was-versie een 'datum JWV'-einde heeft , dan MOET de 'datum JWV' van de wordt-versie eerder dan deze 'datum JWV'-einde zijn.|
|OZON0040|Blokkerend|Als een RegelVoorIedereen verwijst naar een Gebiedsaanwijzing, dan moet deze bestaan.|
|OZON0041|Blokkerend|Als een Instructieregel verwijst naar een Gebiedsaanwijzing, dan moet deze bestaan.|
|OZON0042|Blokkerend|Als een RegelVoorIedereen verwijst naar een Omgevingsnorm, dan moet deze bestaan.|
|STOP1029|Blokkerend|Een doel kan maar één datum inwerkingtreding hebben.|
|STOP1030|Blokkerend|Binnen dezelfde container data:overheidsdomeinen mag een unieke waarde maar één keer worden gebruikt.|
|STOP1031|Blokkerend|Binnen dezelfde container data:onderwerpen mag een unieke waarde maar één keer worden gebruikt.|
|STOP1032|Blokkerend|Een officiële publicatie van een besluit MOET een datum ondertekening hebben.|
|STOP3020|Blokkerend|Coördinaten van een geometrisch object in een GIO MOETEN gebruikmaken van één van de twee ruimtelijke referentiesystemen:RD: srsName='urn:ogc:def:crs:EPSG::28992' ofETRS89: srsName='urn:ogc:def:crs:EPSG::4258'.|
|TPOD2447|Blokkerend|Als soortRegeling = 'Toegangsbeperkingsbesluit' en eindverantwoordelijke van het besluit = waarde uit waardelijst 'Ministerie' dan MOET voor de regeling RegelingKlassiek of RegelingCompact  gebruikt worden.|
|TPOD2512|Blokkerend|Als soortRegeling = 'Waterschapsverordening' dan mag van de waardelijst Type Gebiedsaanwijzing alleen een waarde uit de volgende lijst voorkomen {beperkingengebied, bodem, energievoorziening, erfgoed, geluid, landschap, leiding, natuur, verkeer, water en watersysteem}|
