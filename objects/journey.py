from . import flight_list

class Journey(flight_list.FlightList):

    def isDestinationVisited(self, next_flight): # return False for the place where we started
        for flight in self.flightList:
            if flight.destination == next_flight.destination:
                return True
        return False


    def isTheFlightNextPossible(self, nextFlight, minutesToTransfer):
        if not self.flightList:
            return True
        lastFlight = self.flightList[-1]
        if ((not self.isDestinationVisited(nextFlight)) and \
                lastFlight.isTimeToTransferMoreThan(nextFlight, minutesToTransfer)):
            return True
        return False



    def addFlight(self, flight):
        super().addFlight(flight)
        self.print()

