from market.models import Commodity, Industry
import csv

with open('assets/csv/sctg.csv') as file:
    for row in csv.DictReader(file):
        Commodity.objects.create(sctg_code=row['code'], description=row['desc'], sctg_group=row['group'])

with open('assets/csv/naics.csv') as file:
    for row in csv.DictReader(file):
        Industry.objects.create(naics_code=row['code'], description=row['desc'])
