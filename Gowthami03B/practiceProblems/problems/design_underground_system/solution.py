class UndergroundSystem:

    def __init__(self):
        # self.stations = defaultdict(list)
        self.averages = defaultdict(lambda : [0, 0])
        self.customers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customers:
            start_station, start_time = self.customers[id]
            diff = t - start_time
            # self.stations[(start_station, stationName)].append(diff)
            self.averages[(start_station, stationName)][0] += diff
            self.averages[(start_station, stationName)][1] += 1
            del self.customers[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation,endStation) in self.averages:
            return self.averages[(startStation,endStation)][0]/self.averages[(startStation,endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)