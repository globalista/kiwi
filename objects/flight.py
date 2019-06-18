import datetime


def string_to_datetime(string):
    return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%S')


def datetime_to_string(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


def round_if_possible(fl):
    return '{:,g}'.format(fl)


class Flight:

    def __init__(self, flight_dict):
        self.source = flight_dict['source']
        self.destination = flight_dict['destination']
        self.departure = string_to_datetime(flight_dict['departure'])
        self.arrival = string_to_datetime(flight_dict['arrival'])
        self.flight_number = flight_dict['flight_number']
        self.price = float(flight_dict['price'])
        self.bags_allowed = int(flight_dict['bags_allowed'])
        self.bag_price = float(flight_dict['bag_price'])

    def print(self):
        print(self.source, self.destination,
              datetime_to_string(self.departure), datetime_to_string(self.arrival),
              self.flight_number, round_if_possible(self.price),
              self.bags_allowed, round_if_possible(self.bag_price), sep=',')

    def time_to_transfer(self, next_flight):
        return next_flight.departure - self.arrival
