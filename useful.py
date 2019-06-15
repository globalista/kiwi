from datetime import datetime
import csv, sys


def string_to_datetime(str):
    return datetime.strptime(str, '%Y-%m-%dT%H:%M:%S')

'''
def csvToDicts(csv_file):
    with open(csv_file) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=False)]
    return a
'''

def csv_to_dicts():
    a = [{k: v for k, v in row.items()}
         for row in csv.DictReader(sys.stdin, skipinitialspace=False)]
    print(a)
    return a
