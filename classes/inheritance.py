class Animal:
    def __init__(self, name):
        self._name = name

    def name(self):
        print(self._name)

    def running(self):
        print("Animal is running")

class Cat(Animal):
    def purr(self):
        print("Purring...")


class Dog(Animal):
    def bark(self):
        print("Woof")

c = Cat("Plu")
d = Dog("Rust")
c.running()
d.bark()