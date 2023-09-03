from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    VALID_TYPES = ['Food', 'Drink']
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args):
        players_added = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                players_added.append(player)
        result = ', '.join(p.name for p in players_added)
        return f"Successfully added: {result}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        for player in self.players:
            if player.name == player_name:
                break
        else:
            return

        if sustenance_type not in Controller.VALID_TYPES:
            return

        if player.need_sustenance == False:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies)- 1, -1, -1):
            supply = self.supplies[i]

            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player.stamina + supply.energy > 100:
            player.stamina = 100

        else:
            player.stamina += supply.energy

        return f"{player_name} sustained successfully with {supply.name}."


    def duel(self, first_player_name: str, second_player_name: str):
        current_players = sorted([
            next(filter(lambda x: x.name == first_player_name, self.players)),
            next(filter(lambda x: x.name == second_player_name, self.players))
        ],key = lambda p: p.stamina)

        errors_list = []

        for player in current_players:
            if player.stamina <= 0:
                errors_list.append(f"Player {player.name} does not have enough stamina.")

        if errors_list:
            return '\n'.join(errors_list)

        return self.fight(current_players)

    def fight(self, current_players):
        first_player_damage = current_players[0].stamina / 2

        if current_players[1].stamina <= first_player_damage:
            current_players[1].stamina = 0
            return f"Winner: {current_players[0].name}"

        else:
            current_players[1].stamina -= first_player_damage

        second_player_damage = current_players[1].stamina / 2

        if current_players[0].stamina <= second_player_damage:
            current_players[0].stamina = 0
            return f"Winner: {current_players[1].name}"
        else:
            current_players[0].stamina -= second_player_damage

        winner = sorted(current_players, key = lambda x: -x.stamina)[0]
        return f"Winner: {winner.name}"


    def next_day(self):
        for player in self.players:
            reduce_stamina_with = player.age *2
            player.stamina = max(player.stamina - reduce_stamina_with, 0)

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        return "\n".join(
            [p.__str__() for p in self.players]
                +
            [s.details() for s in self.supplies]
        )



