from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

  EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
  TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

  def __init__(self, name: str, capacity: int):
    self.name = name
    self.capacity = capacity
    self.equipment = []
    self.teams = []

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    if not(value.isalnum()):
      raise ValueError("Tournament name should contain letters and digits only!")
    self.__name = value


  def add_equipment(self, equipment_type: str):
    if equipment_type not in self.EQUIPMENT_TYPES:
      raise Exception("Invalid equipment type!")
    new_equipment = self.EQUIPMENT_TYPES[equipment_type]()
    self.equipment.append(new_equipment)
    return f"{equipment_type} was successfully added."


  def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
    if team_type not in self.TEAM_TYPES:
      raise Exception("Invalid team type!")
    if len(self.teams) >= self.capacity:
      return "Not enough tournament capacity."
    new_team = self.TEAM_TYPES[team_type](team_name, country, advantage)
    self.teams.append(new_team)
    return f"{team_type} was successfully added."

  def sell_equipment(self, equipment_type: str, team_name: str):
    
    current_equipment = [e for e in self.equipment if e.TYPE_ == equipment_type][-1]
    current_team = [t for t in self.teams if t.name == team_name][0]

    if current_team.budget < current_equipment.price:
      raise Exception("Budget is not enough!")

    current_team.equipment.append(current_equipment)
    self.equipment.remove(current_equipment)
    current_team.budget -= current_equipment.price
    return f"Successfully sold {equipment_type} to {team_name}."
    

  def remove_team(self, team_name: str):
    try:
      current_team = next(filter(lambda x: x.name == team_name, self.teams))

      if current_team.wins > 0:
        raise Exception(f"The team has {current_team.wins} wins! Removal is impossible!")

      self.teams.remove(current_team)
      return f"Successfully removed {team_name}."

    except StopIteration:
      raise Exception("No such team!")

  def increase_equipment_price(self, equipment_type: str):
    increased_equipments = len([eq.increase_price() for eq in self.equipment if eq.TYPE_ == equipment_type])
    return f"Successfully changed {increased_equipments}pcs of equipment."

  def play(self, team_name1: str, team_name2: str):
    team_1 = next(filter(lambda x: x.name == team_name1, self.teams))
    team_2 = next(filter(lambda x: x.name == team_name2, self.teams))
    if not(team_1.TYPE_ == team_2.TYPE_):
      raise Exception("Game cannot start! Team types mismatch!")
    team_1_points = team_1.sum_points()
    team_2_points = team_2.sum_points()

    if team_1_points == team_2_points:
      return "No winner in this game."

    elif team_1_points > team_2_points:
      team_1.win()
      return f"The winner is {team_1.name}."
    else:
      team_2.win()
      return f"The winner is {team_2.name}."

  def get_statistics(self):
    sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
    result = "\n".join([t.get_statistics() for t in sorted_teams])
    return f"Tournament: {self.name}\n" +\
            f"Number of Teams: {len(self.teams)}\n" +\
            "Teams:\n" +\
           f"{result}"


