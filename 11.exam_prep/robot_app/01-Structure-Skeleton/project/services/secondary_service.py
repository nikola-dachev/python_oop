
from project.services.base_service import BaseService

class SecondaryService(BaseService):
  TYPE_ = "SecondaryService"
  def __init__(self,name):
    super().__init__(name, capacity = 15)

  def details(self):
    robots = ' '.join([robot.name for robot in self.robots]) if self.robots else "none"
    return f"{self.name} Secondary Service:\n" +\
           f"Robots: {robots}"
