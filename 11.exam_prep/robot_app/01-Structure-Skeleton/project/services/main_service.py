
from project.services.base_service import BaseService

class MainService(BaseService):
  TYPE_ = "MainService"
  def __init__(self,name):
    super().__init__(name, capacity = 30)

  def details(self):
    robots = ' '.join([robot.name for robot in self.robots]) if self.robots else "none"
    return f"{self.name} Main Service:\n" +\
           f"Robots: {robots}"
