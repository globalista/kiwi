from datetime import datetime, timedelta
import csv


def stringToDatetime(str):
    return datetime.strptime('2019-05-11T22:10:00', '%Y-%m-%dT%H:%M:%S')


def datetime_to_string(dt):
    return datetime.strftime(dt)


def csvToDicts(csv_file):
    with open(csv_file) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=False)]
    return a





'''
def make_list_of_flights_next_possible(the_travel, list_of_flights, time_needed_to_transfer):
    flights_next_possible = []
    for next_flight in list_of_flights:
        if next_flight['source'] == the_travel[-1]['destination']:
            if (possible_destination(the_travel, next_flight)) and \
               (time_from_arrival_to_departure_is_more_than(the_travel[-1], next_flight, time_needed_to_transfer)):
                flights_next_possible.append(next_flight)
    return flights_next_possible
'''

