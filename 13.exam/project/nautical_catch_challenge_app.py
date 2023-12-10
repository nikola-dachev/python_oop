from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"DeepSeaFish": DeepSeaFish, "PredatoryFish": PredatoryFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if len([diver for diver in self.divers if diver.name == diver_name]) >0:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVERS_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if len([fish for fish in self.fish_list if fish.name == fish_name]) > 0:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        try:
            diver = next(filter(lambda x: x.name == diver_name, self.divers))

        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda x: x.name == fish_name, self.fish_list))

        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.oxygen_level == 0:
            diver.has_health_issue = True

        if diver.has_health_issue == True:
            return f"{diver.name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver.name} missed a good {fish.name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky == True:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level >fish.time_to_catch:
            self.fish_list.append(fish)
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."


    def health_recovery(self):
        sorted_divers = [diver for diver in self.divers if diver.has_health_issue == True]

        for current_diver in self.divers:
            current_diver.has_health_issue = False
            current_diver.oxygen_level = current_diver.MAX_OXYGEN_LEVEL

        return f"Divers recovered: {len(sorted_divers)}"

    def diver_catch_report(self, diver_name: str):
        diver = [diver for diver in self.divers if diver.name == diver_name][0]
        caught_fish_details = '\n'.join([fish.fish_details() for fish in diver.catch])
        return f"**{diver_name} Catch Report**\n" +\
                 f"{caught_fish_details}"

    def competition_statistics(self):
        divers_in_good_health_condition =[diver for diver in self.divers if diver.has_health_issue == False]
        sorted_divers = sorted(divers_in_good_health_condition,  key= lambda x: ( -x.competition_points, -(len(x.catch)), x.name))
        diver_details = '\n'.join([diver.__str__() for diver in sorted_divers])
        return  "**Nautical Catch Challenge Statistics**\n" +\
                f"{diver_details}"

