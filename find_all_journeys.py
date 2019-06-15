from objects import journey


def find_all_journeys(flight_list, bags_taken, hours_to_transfer_needed):
    if not flight_list.flight_list:
        print('No flights are possible')
    else:
        for flight in flight_list.flight_list:
            new_journey = journey.Journey()
            new_journey.add_flight(flight)
            new_journey.print_with_price_for_bags(bags_taken)
            add_flight_to_journey(new_journey, flight_list, bags_taken, hours_to_transfer_needed)


def add_flight_to_journey(the_journey, flight_list, bags_taken, hours_to_transfer_needed):
    last_flight = the_journey.flight_list[-1]
    flights_from_the_place = flight_list.flights_from_the_source(last_flight.destination)
    for flight in flights_from_the_place.flight_list:
        if the_journey.is_the_flight_next_possible(flight, hours_to_transfer_needed):
            the_journey.add_flight(flight)
            the_journey.print_with_price_for_bags(bags_taken)
            if the_journey.flight_list[0].source != the_journey.flight_list[-1].destination:
                add_flight_to_journey(the_journey, flight_list, bags_taken, hours_to_transfer_needed)
