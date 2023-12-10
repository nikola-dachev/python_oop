

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
  VALID_SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
  VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
  
  def __init__(self):
    self.robots = []
    self.services = []

  def add_service(self, service_type: str, name: str):
    if service_type not in self.VALID_SERVICE_TYPES:
      raise Exception("Invalid service type!")

    new_service = self.VALID_SERVICE_TYPES[service_type](name)
    self.services.append(new_service)
    return f"{service_type} is successfully added."

  def add_robot(self, robot_type: str, name: str, kind: str, price: float):
    if robot_type not in self.VALID_ROBOT_TYPES:
      raise Exception("Invalid robot type!")

    new_robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
    self.robots.append(new_robot)
    return f"{robot_type} is successfully added."

  def add_robot_to_service(self, robot_name: str, service_name: str):
    robot =[robot for robot in self.robots if robot.name == robot_name][0]
    service = [service for service in self.services if service.name == service_name][0]

    if len(service.robots) >= service.capacity:
      raise Exception("Not enough capacity for this robot!")

    if not ((robot.TYPE_ == "FemaleRobot" and service.TYPE_ == "SecondaryService") or (robot.TYPE_ == "MaleRobot" and service.TYPE_ == "MainService")):
      return "Unsuitable service."

    service.robots.append(robot)
    self.robots.remove(robot)
    return f"Successfully added {robot_name} to {service_name}."


  def remove_robot_from_service(self, robot_name: str, service_name: str):
    service = [service for service in self.services if service.name == service_name][0]

    try:
      robot = next(filter(lambda x:x.name == robot_name, service.robots))
      service.robots.remove(robot)
      self.robots.append(robot)
      return f"Successfully removed {robot_name} from {service_name}."

    except StopIteration:
      raise Exception("No such robot in this service!")

  def feed_all_robots_from_service(self, service_name: str):
    service = [service for service in self.services if service.name == service_name][0]
    fed_robots = [robot.eating() for robot in service.robots]
    return f"Robots fed: {len(fed_robots)}."

  def service_price(self, service_name: str):
    service = [service for service in self.services if service.name == service_name][0]
    total_price = sum([robot.price for robot in service.robots])
    return f"The value of service {service_name} is {total_price:.2f}."


  def __str__(self):
    result = '\n'.join([service.details() for service in self.services])
    return result
    
      