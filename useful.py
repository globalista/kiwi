from datetime import datetime
import csv, sys


def stringToDatetime(str):
    return datetime.strptime(str, '%Y-%m-%dT%H:%M:%S')

'''
def csvToDicts(csv_file):
    with open(csv_file) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=False)]
    return a
'''

def csvToDicts():
    a = [{k: v for k, v in row.items()}
         for row in csv.DictReader(sys.stdin, skipinitialspace=False)]
    print(a)
    return a
