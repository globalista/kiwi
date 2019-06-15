from useful import string_to_datetime

class Flight:

    def __init__(self, flight_dict):
        self.source = flight_dict['source']
        self.destination = flight_dict['destination']
        self.departure = flight_dict['departure']
        self.arrival = flight_dict['arrival']
        self.flight_number = flight_dict['flight_number']
        self.price = flight_dict['price']
        self.bags_allowed = flight_dict['bags_allowed']
        self.bags_price = flight_dict['bag_price']


    def print(self):
        print(self.source, self.destination, self.departure, self.arrival, self.flight_number,
              self.price, self.bags_allowed, self.bags_price, sep=',')


    def time_to_transfer(self, next_flight):
        return string_to_datetime(next_flight.departure) - string_to_datetime(self.arrival)