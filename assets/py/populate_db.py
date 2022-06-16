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
        MarketArea.objects.create(core=row['center'], state=row['state'], country=row['country'])

with open('assets/csv/csa.csv') as file:
    for row in csv.DictReader(file):
        StatArea.objects.create(core=row['csa'], state=row['state'], code=row['csa_code'], fips=row['state_code'])

with open('assets/csv/dma.csv') as file:
    for row in csv.DictReader(file):
        MetroArea.objects.create(core=row['core'], state=row['state'], code=row['code'], fips=row['fips'])
