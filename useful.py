from datetime import datetime
import csv


def string_to_datetime(str):
    return datetime.strptime(str, '%Y-%m-%dT%H:%M:%S')

'''
def csvToDicts(csv_file):
    with open(csv_file) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=False)]
    return a
'''

def csv_to_dicts(csv_input):
    a = [{k: v for k, v in row.items()}
         for row in csv.DictReader(csv_input, skipinitialspace=False)]
    return a
