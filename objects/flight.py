import datetime

def string_to_datetime(str):
    return datetime.datetime.strptime(str, '%Y-%m-%dT%H:%M:%S')

def datetime_to_string(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

class Flight:

    def __init__(self, flight_dict):
        self.source = flight_dict['source']
        self.destination = flight_dict['destination']
        self.departure = string_to_datetime(flight_dict['departure'])
        self.arrival = string_to_datetime(flight_dict['arrival'])
        self.flight_number = flight_dict['flight_number']
        self.price = float(flight_dict['price'])
        self.bags_allowed = int(flight_dict['bags_allowed'])
        self.bags_price = float(flight_dict['bag_price'])


    def print(self):
        print(self.source, self.destination, datetime_to_string(self.departure),
              datetime_to_string(self.arrival), self.flight_number,
              self.price, self.bags_allowed, self.bags_price, sep=',')


    def time_to_transfer(self, next_flight):
        return next_flight.departure - self.arrival

