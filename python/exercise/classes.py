class factory:
    def __init__(self, speed):
        self.speed = speed
        self.fuel = 100
        self.km = 0

    def travel(self, inp):
        self.fuel = self.fuel - inp/5
        self.km = self.km + inp * self.speed


car = factory(200)
car.travel(20)
print(car.fuel)
print(car.km)