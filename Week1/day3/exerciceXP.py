# EXERCICE 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Moustache", 4)
cat2 = Cat("Felix", 7)
cat3 = Cat("Minette", 2)


def find_oldest_cat(cats_list):

    return max(cats_list, key=lambda cat: cat.age)


cats = [cat1, cat2, cat3]
oldest_cat = find_oldest_cat(cats)


print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.\n")


# EXERCICE 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(f"David's dog: name = {davids_dog.name}, height = {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog: name = {sarahs_dog.name}, height = {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print("Both dogs are the same height!")
print()


# EXERCICE 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(
    [
        "There’s a lady who's sure",
        "all that glitters is gold",
        "and she’s buying a stairway to heaven",
    ]
)

stairway.sing_me_a_song()
print()


# EXERCICE 4
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")

    def add_animals(self, *args):
        for animal in args:
            if animal not in self.animals:
                self.animals.append(animal)
                print(f"{animal} has been added to the zoo.")
            else:
                print(f"{animal} is already in the zoo.")

    def get_animals(self):
        if not self.animals:
            print("The zoo is empty.")
        else:
            print(f"Animals in {self.zoo_name} zoo:")
            for animal in self.animals:
                print(f"  - {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold and leaves the zoo.")
        else:
            print(f"{animal_sold} is not in the zoo, cannot sell.")

    def sort_animals(self):
        if not self.animals:
            return {}
        sorted_animals = sorted(self.animals)
        groups = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        if not groups:
            print("No animals to group.")
        else:
            print(f"Animal groups for {self.zoo_name} zoo:")
            for letter, animals in sorted(groups.items()):
                print(f"  {letter}: {animals}")


my_zoo = Zoo("Mon Petit Zoo")

my_zoo.add_animal("Giraffe")
my_zoo.add_animal("Bear")
my_zoo.add_animal("Baboon")
my_zoo.add_animal("Cat")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Zebra")
my_zoo.add_animal("Giraffe")

print()
my_zoo.get_animals()
print()

my_zoo.sell_animal("Bear")
my_zoo.get_animals()
print()

groups = my_zoo.sort_animals()
print("Groups dictionary:", groups)
print()

my_zoo.get_groups()
print()

my_zoo.add_animals("Panda", "Koala", "Tiger")
my_zoo.get_animals()
print()


class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal, count=1):

        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def add_multiple(self, **kwargs):

        for animal, count in kwargs.items():
            self.add_animal(animal, count)

    def get_info(self):

        info = f"{self.name}'s farm\n"
        for animal, cnt in self.animals.items():
            info += f"{animal} : {cnt}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_most_populous(self):

        if not self.animals:
            return None
        return max(self.animals, key=lambda animal: self.animals[animal])

    def get_animal_types(self):

        return sorted(self.animals.keys())

    def get_short_info(self):

        types = self.get_animal_types()

        animal_names = []
        for animal in types:
            count = self.animals[animal]
            if count > 1:
                animal_names.append(animal + "s")
            else:
                animal_names.append(animal)

        if len(animal_names) == 1:
            animals_str = animal_names[0]
        else:
            animals_str = ", ".join(animal_names[:-1]) + " and " + animal_names[-1]
        return f"{self.name}'s farm has {animals_str}."


macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)

print(macdonald.get_info())
print()
print("Most populous animal:", macdonald.get_most_populous())
print()
print(macdonald.get_short_info())

farm2 = Farm("Old MacDonald")
farm2.add_multiple(cow=5, sheep=2, goat=12)
print(farm2.get_info())
print()
print(farm2.get_short_info())
