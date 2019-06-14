import useful
from objects import flightList
from findAllJourneys import findAllJourneys


def get_parameters():

    bagsTaken = int(input('How many bags do you want to take? (0-2) '))
    minutesToTransferNeeded = int(input('How many hours do you need to transfer? (1-3)'))
    print()
    return bagsTaken, minutesToTransferNeeded




def initializeSearch():
    flightDicts = useful.csvToDicts()
    allFlights = flightList.FlightList()
    allFlights.uploadDict(flightDicts)
    bagsTaken, minutesToTransferNeeded = get_parameters()
    allPossFlights = allFlights.flightsByBagsTaken(bagsTaken)
    findAllJourneys(allPossFlights, bagsTaken, minutesToTransferNeeded)



