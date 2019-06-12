import useful
from objects import journey, flight_list
from copy import deepcopy


def findAllJourneys(flightList, minutesToTransferNeeded):
    if not flightList.flightList:
        print('No flights are possible')
    else:
        for flight in flightList.flightList:
            newJourney = journey.Journey()
            newJourney.addFlight(flight)
            newJourney.print()
            addFlightToJourney(newJourney, flightList, minutesToTransferNeeded)


def addFlightToJourney(theJourney, flightList, minutesToTransferNeeded):
    lastFlight = theJourney.flightList[-1]
    flightsFromThePlace = flightList.flightsFromTheSource(lastFlight.destination)
    #flightsFromThePlace.print()
    for flight in flightsFromThePlace.flightList:
        if theJourney.isTheFlightNextPossible(flight, minutesToTransferNeeded):
            theJourney.addFlight(flight)
            theJourney.print()
            if theJourney.flightList[0].source != theJourney.flightList[-1].destination:
                addFlightToJourney(theJourney, flightList, minutesToTransferNeeded)



def initializeSearch(csvInput, bagsTaken, minutesToTransferNeeded):
    flightDicts = useful.csvToDicts(csvInput)
    allFlights = flight_list.FlightList()
    allFlights.uploadDict(flightDicts)
    allPossFlights = allFlights.flightsByBagsTaken(bagsTaken)
    findAllJourneys(allPossFlights, minutesToTransferNeeded)





