from market.models import *
import csv

with open('assets/csv/sctg.csv') as file:
    for row in csv.DictReader(file):
        Commodity.objects.create(sctg_code=row['code'], description=row['desc'], sctg_group=row['group'])

with open('assets/csv/naics.csv') as file:
    for row in csv.DictReader(file):
        Industry.objects.create(naics_code=row['code'], description=row['desc'])

with open('assets/csv/kma.csv') as file:
    for row in csv.DictReader(file):
        MarketArea.objects.create(center=row['center'], state=row['state'], country=row['country'])

with open('assets/csv/csa.csv') as file:
    for row in csv.DictReader(file):
        StatArea.objects.create(csa_name=row['csa'], state=row['state'], csa_code=row['csa_code'], state_code=row['state_code'])
