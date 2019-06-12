from inputs import conditions
import useful
from find_all_journeys import initializeSearch

bags_taken = conditions.BAGS_TAKEN
minutes_to_transfer_needed = conditions.MINUTES_TO_TRANSFER_NEEDED
csv_input = conditions.CSV_INPUT


print(bags_taken, minutes_to_transfer_needed)
dicts = useful.csvToDicts(csv_input)
print(dicts)

    
initializeSearch(csv_input, bags_taken, minutes_to_transfer_needed)
