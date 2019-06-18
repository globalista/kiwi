from objects import flight


class FlightList:

    def __init__(self):
        self.flight_list = []

    def add_flight(self, new_flight):
        self.flight_list.append(new_flight)

    def print(self):
        for i in self.flight_list:
            i.print()

    def upload_dicts(self, flight_dicts):
        for i in flight_dicts:
            new_flight = flight.Flight(i)
            self.add_flight(new_flight)

    def flights_by_bags_taken(self, bags_taken):
        new_flight_list = FlightList()
        for fl in self.flight_list:
            if int(fl.bags_allowed) >= bags_taken:
                new_flight_list.add_flight(fl)
        return new_flight_list

    def flights_from_the_source(self, place):
        new_flight_list = FlightList()
        for fl in self.flight_list:
            if fl.source == place:
                new_flight_list.add_flight(fl)
        return new_flight_list
