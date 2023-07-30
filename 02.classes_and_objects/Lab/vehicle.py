class Vehicle:
  def __init__(self, mileage, max_speed = 150 ):
    self.max_speed = max_speed
    self.mileage = mileage
    self.gadgets =[]

car = Vehicle(100000, 200)
car_2 = Vehicle(1900000)