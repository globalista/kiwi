from useful import stringToDatetime
# from datetime import timedelta

class Flight:

    def __init__(self, flightDict):
        self.source = flightDict['source']
        self.destination = flightDict['destination']
        self.departure = flightDict['departure']
        self.arrival = flightDict['arrival']
        self.flightNumber = flightDict['flight_number']
        self.price = flightDict['price']
        self.bagsAllowed = flightDict['bags_allowed']
        self.bagPrice = flightDict['bag_price']


    def print(self):
        for i in [self.source, self.destination, self.departure, self.arrival, self.flightNumber,
                  self.price, self.bagsAllowed]:
            print(i, end=',')
        print(self.bagPrice)


    '''
    def isTimeToTransferMoreThan(self, flight2, td):
        timeBetweenFlights = stringToDatetime(flight2.departure) - stringToDatetime(self.arrival)
        if timeBetweenFlights > timedelta(minutes=td):
            return True
        return False
    '''

    def timeToTransfer(self, next_flight):
        return stringToDatetime(next_flight.departure) - stringToDatetime(self.arrival)