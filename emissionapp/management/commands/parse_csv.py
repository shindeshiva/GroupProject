import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from emissionapp.models import project

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        project.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/emissionapp/emissioncsvfile/golfproject.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                table1 = project.objects.create(
                serialNo = row[0],
                country = row[1],
                isocode = row[2],
                year = row[3]
                )
                table1.save()
        



        # drop the data from the table so that if we rerun the file, we don't repeat values
        project.objects.all().delete()
        print("table dropped successfully")

        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/emissionapp/emissioncsvfile/golfproject.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                table2 = project.objects.create(
                serialNo = row[0],
                total = row[4],
                coal = row[5],
                oil = row[6],
                gas = row[7],
                cement = row[8],
                flaring = row[9],
                other = row[10]
                )
                table2.save()
        print("data parsed successfully")