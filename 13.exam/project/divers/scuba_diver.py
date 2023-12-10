from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    TYPE_ = "ScubaDiver"
    MAX_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, oxygen_level = 540)

    def miss(self, time_to_catch: int):

        if self.oxygen_level - round(0.3 * time_to_catch) > 0:
            self.oxygen_level -= round(0.3 * time_to_catch)
        if self.oxygen_level - round(0.3 * time_to_catch) < 0:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = 540

    def __str__(self):
        return f"{self.TYPE_}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"