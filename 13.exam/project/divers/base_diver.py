from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        # the fish that has been caught by the particular diver
        self.catch = []
        # the total points accumulated by a diver, based on the type of fish caught  rounded  to :.1f
        self.competition_points = 0
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level - fish.time_to_catch >0:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points += round(fish.points, 1)
        else:
            self.oxygen_level = 0
            self.catch.append(fish)
            self.competition_points += round(fish.points, 1)

# old code
#         self.oxygen_level -= fish.time_to_catch
#         if self.oxygen_level <0:
#             self.oxygen_level = 0
#         else:
#             self.catch.append(fish)
#             self.competition_points += round(fish.points, 1)

    def update_health_status(self):
        if self.has_health_issue == True:
            self.has_health_issue = False
        else:
            self.has_health_issue = True

    @abstractmethod
    def __str__(self):
        pass

