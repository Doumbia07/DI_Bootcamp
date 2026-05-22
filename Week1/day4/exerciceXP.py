# EXERCICE 1


class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Siamese(Cat):
    pass


bengal_obj = Bengal("Simba", 3)
chartreux_obj = Chartreux("Felix", 2)
siamese_obj = Siamese("Luna", 4)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]


sara_pets = Pets(all_cats)

sara_pets.walk()


# EXERCICE 2


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}"
        else:
            return f"{other_dog.name} won the fight against {self.name}"


dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Max", 7, 25)

# Step 3: Test Dog methods

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog3.fight(dog1))


# EXERCICE 3
import random


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join(args)
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead",
            ]
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")


# Step 3: Test PetDog methods

my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()
print("\n")


# EXERCICE 4
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No person named {first_name} found in the family.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        for person in self.members:
            print(f"{person.first_name} is {person.age} years old")


my_family = Family("Smith")
my_family.born("Alice", 17)
my_family.born("Bob", 19)
my_family.born("Charlie", 25)

my_family.family_presentation()
print("\n--- Check majority ---")
my_family.check_majority("Alice")
my_family.check_majority("Bob")
my_family.check_majority("Charlie")
