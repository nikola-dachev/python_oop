from project.vehicles.base_vehicle import BaseVehicle 


class CargoVan(BaseVehicle):
  TYPE_ = "CargoVan"
  def __init__(self, brand: str, model: str, license_plate_number: str):
    super().__init__(brand, model, license_plate_number, max_mileage = 180.00)

  def drive(self, mileage:float):
    passed_mileage = round((mileage / 180.00) * 100)
    passed_mileage += 5
    self.battery_level -= passed_mileage
