import useful


def do_the_next_step(the_travel, list_of_all_flights):
    f.





def finding_all_travels(csv_input, bags_taken, minutes_to_transfer_needed):
    list_of_dict_of_flights = useful.csv_to_list_of_dicts(csv_input)
    list_of_flights_account_baggage = useful.remove_flights_by_bags_allowed(list_of_dict_of_flights, bags_taken)
    f= open("home/vladena/python/kiwi/output/result.txt","w+")
    for flight in list_of_flights_account_baggage:
        new_travel = [flight]
        do_the_next_step(new_travel)




