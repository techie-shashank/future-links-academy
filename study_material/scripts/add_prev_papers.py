import csv
import requests
from io import BytesIO

from django.core import files

from study_material import models as study_material_models


def add_papers(file_path='output.csv'):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        csvfile.seek(0)
        counter = 0
        for row in reader:
            url = "https://flacademy.s3.amazonaws.com/media/media/" + row['Name']
            set_no = row['Set']
            std = int(row['Class'])
            sub = int(row['Subject'])
            year = int(row['Year'])
            resp = requests.get(url)
            fp = BytesIO()
            fp.write(resp.content)
            file_name = url.split("/")[-1]
            a = study_material_models.PreviousYearPapers(
                subject=sub, standard=std, set_no=set_no, year=year
            )
            a.file.save(file_name, files.File(fp))
            a.save()
            counter += 1
            print(counter)

