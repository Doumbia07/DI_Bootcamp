class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Moustache", 4)
cat2 = Cat("Felix", 7)
cat3 = Cat("Minette", 2)


def find_oldest_cat(cat_a, cat_b, cat_c):
    oldest = cat_a
    if cat_b.age > oldest.age:
        oldest = cat_b
    if cat_c.age > oldest.age:
        oldest = cat_c
    return oldest


oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# EXERCICE 1
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.\n")


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# EXERCICE 2
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

# EXERCICE 3
stairway.sing_me_a_song()
print()


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} a été ajouté au zoo.")
        else:
            print(f"{new_animal} est déjà dans le zoo.")

    def add_animals(self, *args):
        for animal in args:
            if animal not in self.animals:
                self.animals.append(animal)
                print(f"{animal} a été ajouté au zoo.")
            else:
                print(f"{animal} est déjà dans le zoo.")

    def get_animals(self):
        if not self.animals:
            print("Le zoo est vide.")
        else:
            print(f"Animaux dans le zoo {self.zoo_name} :")
            for animal in self.animals:
                print(f"  - {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu et quitte le zoo.")
        else:
            print(f"{animal_sold} n'est pas dans le zoo, impossible de le vendre.")

    def sort_animals(self):
        if not self.animals:
            return {}
        animaux_tries = sorted(self.animals)
        groupes = {}
        for animal in animaux_tries:
            premiere_lettre = animal[0].upper()
            if premiere_lettre not in groupes:
                groupes[premiere_lettre] = []
            groupes[premiere_lettre].append(animal)
        return groupes

    def get_groups(self):
        groupes = self.sort_animals()
        if not groupes:
            print("Aucun animal à grouper.")
        else:
            print(f"Groupes d'animaux pour le zoo {self.zoo_name} :")
            for lettre, animaux in sorted(groupes.items()):
                print(f"  {lettre}: {animaux}")


# EXERCICE 4

my_zoo = Zoo("Mon Petit Zoo")

my_zoo.add_animal("Girafe")
my_zoo.add_animal("Ours")
my_zoo.add_animal("Babouin")
my_zoo.add_animal("Chat")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Zèbre")
my_zoo.add_animal("Girafe")

print()
my_zoo.get_animals()
print()

my_zoo.sell_animal("Ours")
my_zoo.get_animals()
print()

groupes = my_zoo.sort_animals()
print("Dictionnaire des groupes :", groupes)
print()

my_zoo.get_groups()
print()

my_zoo.add_animals("Panda", "Koala", "Tigre")
my_zoo.get_animals()
