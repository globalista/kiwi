import useful
from objects import flight_list
from find_all_journeys import find_all_journeys

def initializeSearch():
    flight_dicts = useful.csv_to_dicts()
    all_flights = flight_list.FlightList()
    all_flights.upload_dicts(flight_dicts)
    bags_taken, hours_to_transfer_needed = 2, 1
    all_poss_flights = all_flights.flights_by_bags_taken(bags_taken)
    find_all_journeys(all_poss_flights, bags_taken, hours_to_transfer_needed)



