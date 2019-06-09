from datetime import datetime, timedelta
import csv


def string_to_datetime(str):
    return datetime.strptime('2019-05-11T22:10:00', '%Y-%m-%dT%H:%M:%S')


def datetime_to_string(dt):
    return datetime.strftime(dt)


def csv_to_list_of_dicts(csv_file):
    with open(csv_file) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=False)]
    return a


def time_from_arrival_to_departure_is_less_than(flight1, flight2, td):
    return string_to_datetime(flight2['departure'] - flight1['arrival']) < td


def remove_flights_by_bags_allowed(list_of_flights, bags_count):
    new_list = []
    for flight in list_of_flights:
        if flight['bags_allowed'] > bags_count:
            new_list.append(flight)
    return new_list


def possible_destination(travel, next_flight):
    for flight in travel:
        if flight['destination'] == next_flight['destination']:
            return False
    return True


def make_list_of_flights_next_possible(list_of_all_flights, the_travel, time_needed_to_transfer):
    flights_next_possible = []
    for next_flight in list_of_all_flights:
        if (possible_destination(the_travel, next_flight)) and \
           (time_from_arrival_to_departure_is_less_than(the_travel[-1], next_flight, time_needed_to_transfer)):
            flights_next_possible.append()
    return flights_next_possible

