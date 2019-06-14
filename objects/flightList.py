from objects import flight


class FlightList:

    def __init__(self):
        self.flightList = []


    def addFlight(self, newFlight):
        self.flightList.append(newFlight)


    def print(self):
        for i in self.flightList:
            i.print()

    def uploadDict(self, flightDictList):
        for i in flightDictList:
            newFlight = flight.Flight(i)
            self.addFlight(newFlight)


    def flightsByBagsTaken(self, bagsTaken):
        newFlightList = FlightList()
        for flight in self.flightList:
            if int(flight.bagsAllowed) >= bagsTaken:
                newFlightList.addFlight(flight)
        return newFlightList


    def flightsFromTheSource(self, place):
        newFlightList = FlightList()
        for flight in self.flightList:
            if flight.source == place:
                newFlightList.addFlight(flight)
        return newFlightList




