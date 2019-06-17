from objects import flight_list
from find_all_journeys import find_all_journeys
import sys, csv

def csv_stdin_to_dicts():
    a = [{k: v for k, v in row.items()}
         for row in csv.DictReader(sys.stdin, skipinitialspace=False)]
    return a

def initialize_search(bags_taken, hours_to_transfer_needed):
    flight_dicts = csv_stdin_to_dicts()
    all_flights = flight_list.FlightList()
    all_flights.upload_dicts(flight_dicts)
    all_poss_flights = all_flights.flights_by_bags_taken(bags_taken)
    find_all_journeys(all_poss_flights, bags_taken, hours_to_transfer_needed)



