from datetime import datetime, timedelta
import csv


def stringToDatetime(str):
    return datetime.strptime(str, '%Y-%m-%dT%H:%M:%S')


def datetime_to_string(dt):
    return datetime.strftime(dt)


def csvToDicts(csv_file):
    with open(csv_file) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=False)]
    return a

