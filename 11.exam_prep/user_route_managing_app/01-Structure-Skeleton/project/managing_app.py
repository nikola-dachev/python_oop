
from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
  VALID_VEHICLES_TYPES = {"CargoVan": CargoVan, "PassengerCar": PassengerCar}
  def __init__(self):
    self.users = []
    self.vehicles = []
    self.routes = []

    
  def register_user(self, first_name: str, last_name: str, driving_license_number: str):
    if len([user for user in self.users if user.driving_license_number == driving_license_number]) != 0:
      return f"{driving_license_number} has already been registered to our platform."
      
    new_user = User(first_name, last_name, driving_license_number)
    self.users.append(new_user)
    return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

  def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
    if vehicle_type not in self.VALID_VEHICLES_TYPES:
      return f"Vehicle type {vehicle_type} is inaccessible."

    if len([v for v in self.vehicles if v.license_plate_number == license_plate_number]) !=0:
      return f"{license_plate_number} belongs to another vehicle."

    vehicle = self.VALID_VEHICLES_TYPES[vehicle_type](brand, model, license_plate_number)
    self.vehicles.append(vehicle)
    return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."


  def allow_route(self, start_point: str, end_point: str, length: float):
    
    if len([r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length == length]) != 0:
      return f"{start_point}/{end_point} - {length} km had already been added to our platform."
      
    if len([r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length < length]) != 0:
      return f"{start_point}/{end_point} shorter route had already been added to our platform."
      
    f_route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length > length]
    if len(f_route) != 0:
      f_route[0].is_locked = True  
      
    new_route = Route(start_point, end_point, length, len(self.routes)+1)
    self.routes.append(new_route)
    return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

  def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
    
    current_user = [user for user in self.users if user.driving_license_number == driving_license_number][0]
    if current_user.is_blocked == True:
      return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

    current_vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
    if current_vehicle.is_damaged == True:
      return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

    current_route = [r for r in self.routes if r.route_id == route_id][0]
    if current_route.is_locked == True:
      return f"Route {route_id} is locked! This trip is not allowed."

    current_vehicle.drive(current_route.length)

    if is_accident_happened == True:
      current_vehicle.is_damaged = True
      current_user.decrease_rating()

    else:
      current_user.increase_rating()
      
    status = "OK" if current_vehicle.is_damaged == False else "Damaged"
    return f"{current_vehicle.brand} {current_vehicle.model} License plate: {current_vehicle.license_plate_number} Battery: {current_vehicle.battery_level}% Status: {status}"

  def repair_vehicles(self, count: int):
    damaged_vehicles = [v for v in self.vehicles if v.is_damaged == True]
    sorted_vehicles= sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))[:count]
    for vehicle in sorted_vehicles:
      vehicle.is_damaged = False
      vehicle.battery_level = 100
    return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

  def users_report(self):
        result = ["*** E-Drive-Rent ***", ]
        sorted_users = sorted(self.users, key=lambda user: -user.rating)
        result.append(('\n'.join(str(user) for user in sorted_users)))
        return '\n'.join(result)