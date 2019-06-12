import useful
from objects import journey, flight_list
from copy import deepcopy


def addFlightToJourney(journey, flightList, minutesToTransferNeeded):
    if not journey.flightList:
        if not flightList.flightList:
            print('No flights are possible')
        else:
            for flight in flightList.flightList:
                journey.addFlight(flight)
                addFlightToJourney(deepcopy(journey), flightList, minutesToTransferNeeded)
    else:
        print('dostaneme se az sem?')
        lastFlight = journey.flightList[-1]
        flightsFromThePlace = flightList.flightsFromTheSource(lastFlight.destination)
        for flight in flightsFromThePlace.flightList:
            if journey.isTheFlightNextPossible(flight, minutesToTransferNeeded):
                journey.addFlight(flight)
                addFlightToJourney(deepcopy(journey), flightList, minutesToTransferNeeded)



def findAllJourneys(csvInput, bagsTaken, minutesToTransferNeeded):
    flightDicts = useful.csvToDicts(csvInput)
    allFlights = flight_list.FlightList()
    allFlights.uploadDict(flightDicts)
    allPossFlights = allFlights.flightsByBagsTaken(bagsTaken)
    allPossFlights.print()
    newJourney = journey.Journey()
    addFlightToJourney(newJourney, allPossFlights, minutesToTransferNeeded)





