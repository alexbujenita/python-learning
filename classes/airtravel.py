"""Model for aircraft flights"""

class Flight:

    def __init__(self, number): # __init__ is an initializer and not a constructor
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9000):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number # underscore to avoid name clashes, also convention
    
    def number(self): # self is the first argument to all instance methods, don't need to pass it from a class instance
        return self._number
    
    def airline(self):
        return self._number[:2]




f = Flight("CB060")
print(f.number())
print(f.airline())
f = Flight("CB32344")