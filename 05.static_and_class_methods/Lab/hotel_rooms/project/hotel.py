from typing import List
from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: str, people: int):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))
            room.take_room(people)

        except StopIteration:
            pass

    def free_room(self, room_number: int):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))
            room.free_room()

        except StopIteration:
            pass

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if room.is_taken == False]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken == True]
        return f"Hotel {self.name} has {self.guests} total guests\n" + \
            f"Free rooms: {', '.join(free_rooms)}\n" + \
            f"Taken rooms: {', '.join(taken_rooms)}"
