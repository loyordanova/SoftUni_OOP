from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        if not room.is_taken and room.capacity >= people:
            room.is_taken = True
            self.guests += people

    def free_room(self, room_number: int):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        if room.is_taken:
            room.is_taken = False
            self.guests = 0

    def status(self):
        free_rooms = ', '.join([str(room.number) for room in self.rooms if not room.is_taken])
        taken_rooms = ', '.join([str(room.number) for room in self.rooms if room.is_taken])
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {free_rooms}\n"
                f"Taken rooms: {taken_rooms}")