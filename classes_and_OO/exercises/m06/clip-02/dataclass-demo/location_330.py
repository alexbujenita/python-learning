from dataclasses import dataclass

from position import Position, EarthPosition

from auto_repr import auto_repr


@auto_repr
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.name == other.name) and (self.position == other.position)

    def __hash__(self):
        return hash((self.name, self.position))


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))
