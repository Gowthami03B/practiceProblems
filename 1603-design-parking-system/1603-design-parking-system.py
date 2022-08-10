class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big =big
        self.small=small
        self.medium=medium
        self.occupied_big=0
        self.occupied_small=0
        self.occupied_medium=0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.occupied_big == self.big:
                return False
            self.occupied_big +=1
            return True
        elif carType == 2:
            if self.occupied_medium == self.medium:
                return False
            self.occupied_medium +=1
            return True
        elif carType == 3:
            if self.occupied_small == self.small:
                return False
            self.occupied_small +=1
            return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)