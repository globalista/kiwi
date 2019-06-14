from . import flightList
from datetime import timedelta

class Journey(flightList.FlightList):

    def isDestinationVisited(self, next_flight): # return False for the place where we started
        for flight in self.flightList:
            if flight.destination == next_flight.destination:
                return True
        return False


    def isTheFlightNextPossible(self, nextFlight, timeToTransfer):
        if not self.flightList:
            return True
        lastFlight = self.flightList[-1]
        if self.isDestinationVisited(nextFlight):
            return False
        return lastFlight.timeToTransfer(nextFlight) >= timedelta(hours=timeToTransfer)

    def priceForOneBag(self):
        return sum([int(x.price) for x in self.flightList])

    def printWithPriceForBags(self, bagsTaken):
        super().print()
        print(bagsTaken * self.priceForOneBag(), end='$\n\n')

