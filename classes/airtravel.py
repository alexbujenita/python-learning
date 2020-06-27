from pprint import pprint as pp
"""Model for aircraft flights"""


class Flight:

    def __init__(self, number, aircraft):  # __init__ is an initializer and not a constructor
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9000):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number  # underscore to avoid name clashes, also convention
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + \
            [{letter: None for letter in seats} for _ in rows]

    def _parse_seat(self, seat):  # underscore because the method is an implementation detail
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))
        

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating
                    if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))
    
    def number(self): # self is the first argument to all instance methods, don't need to pass it from a class instance
        return self._number
    
    def airline(self):
        return self._number[:2]
    
    def aircraft_model(self):
        return self._aircraft.model()


class Aircraft:
    def __init__(self, reg, model, num_rows, num_seats_per_row):
        self._reg = reg
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
    
    def registration(self):
        return self._reg
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])
        

# f = Flight("CB060")
# print(f.number())
# print(f.airline())
# test

def console_card_printer(passenger, seat, flight_num, aircraft):
    output = "| Name: {0}"      \
             "  Flight: {1}"    \
             " Seat: {2}"       \
             " Aircraft: {3}"   \
             " |".format(passenger, flight_num, seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

a = Aircraft("G-EUPT", "Airbus A320", num_rows=22, num_seats_per_row=6)
print(a.seating_plan())
print("\n"*2)
f2 = Flight("CB039", Aircraft("G-EUPT", "Airbus A360", num_rows=22, num_seats_per_row=6))
print(f2.aircraft_model())
# print("\n"*2)
# pp(f2._seating)
# print("\n"*2)
f2.allocate_seat("12A", "Alex")
f2.allocate_seat("12B", "Ana")
f2.allocate_seat("12C", "Jebus")
print("\n"*2)
pp(f2._seating)
print("\n"*2)
f2.relocate_passenger("12C", "17D")
pp(f2._seating)
print("\n"*2)
print(f2.num_available_seats())
f2.make_boarding_cards(console_card_printer)