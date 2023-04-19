class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


def animal_sounds(animal):
    print(animal.make_sound())


if __name__ == "__main__":
    dog = Dog("Fido")
    cat = Cat("Fluffy")

    animal_sounds(dog)  # prints "Woof!"
    animal_sounds(cat)  # prints "Meow!"
