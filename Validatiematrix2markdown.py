#!/usr/bin/python3
#
# File: Validatriematrix2markdown.py
#
# Omschrijving: De validatiematrix wordt beheerd in een excel document en gepubliceerd als markdown.
# Dit script doet de conversie.
#
# Auteur: w.quak@geonovum.nl


from datetime import datetime
import openpyxl
import sys

outfile = open('04-Validatiematrix.md','w')

print("""
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
|:--------------|:------|:------------|""",file=outfile)

wb = openpyxl.load_workbook('Validatiematrix.xlsx')
sheet = wb['Validatieregels']
for row in sheet.iter_rows():
    if row[1].value == 'Id' :
        continue

    id = str(row[1].value) 
    ernst = str(row[4].value)
    if ernst != 'Blokkerend' and ernst != 'Waarschuwing':
        print("ERROR: ernst moet 'Blokkerend' of 'Waarschuwing' zijn voor: " + id, file=sys.stderr)
    regel = row[2].value.replace('\n',' ').replace('<','&lt;').replace('>','&gt;')
    print('|' + id + '|' + ernst + '|' + regel + '|',file=outfile)
outfile.close()
