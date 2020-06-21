"""Model for aircraft flights"""

class Flight:

    def __init__(self, number, aircraft): # __init__ is an initializer and not a constructor
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9000):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number # underscore to avoid name clashes, also convention
        self._aircraft = aircraft
    
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

a = Aircraft("G-EUPT", "Airbus A320", num_rows=22, num_seats_per_row=6)
print(a.seating_plan())
print("\n"*2)
f2 = Flight("CB039", Aircraft("G-EUPT", "Airbus A360", num_rows=22, num_seats_per_row=6))
print(f2.aircraft_model())