from objects import journey

def findAllJourneys(flightList, bagsTaken, minutesToTransferNeeded):
    if not flightList.flightList:
        print('No flights are possible')
    else:
        for flight in flightList.flightList:
            newJourney = journey.Journey()
            newJourney.addFlight(flight)
            newJourney.printWithPriceForBags(bagsTaken)
            addFlightToJourney(newJourney, flightList, bagsTaken, minutesToTransferNeeded)


def addFlightToJourney(theJourney, flightList, bagsTaken, minutesToTransferNeeded):
    lastFlight = theJourney.flightList[-1]
    flightsFromThePlace = flightList.flightsFromTheSource(lastFlight.destination)
    for flight in flightsFromThePlace.flightList:
        if theJourney.isTheFlightNextPossible(flight, minutesToTransferNeeded):
            theJourney.addFlight(flight)
            theJourney.printWithPriceForBags(bagsTaken)
            if theJourney.flightList[0].source != theJourney.flightList[-1].destination:
                addFlightToJourney(theJourney, flightList, bagsTaken, minutesToTransferNeeded)








