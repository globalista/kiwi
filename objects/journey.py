from . import flight_list
from datetime import timedelta

class Journey(flight_list.FlightList):

    def is_destination_visited(self, next_flight): # return False for the place where we started
        for flight in self.flight_list:
            if flight.destination == next_flight.destination:
                return True
        return False


    def is_the_flight_next_possible(self, next_flight, time_to_transfer):
        if not self.flight_list:
            return True
        last_flight = self.flight_list[-1]
        if self.is_destination_visited(next_flight):
            return False
        return last_flight.time_to_transfer(next_flight) >= timedelta(hours=time_to_transfer)

    def price_for_one_bag(self):
        return sum([x.bag_price for x in self.flight_list])

    def print_with_price_for_bags(self, bags_taken):
        super().print()
        print('Total price for baggage:',f'{bags_taken * self.price_for_one_bag():.2f}', end='\n\n')

