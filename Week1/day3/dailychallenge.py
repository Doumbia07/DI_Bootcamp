class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        if animal_type is not None:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        for animal, cnt in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += cnt
            else:
                self.animals[animal] = cnt

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, cnt in self.animals.items():
            info += f"{animal} : {cnt}\n"
        info += "    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_list = []
        for animal in animal_types:
            count = self.animals[animal]
            if count > 1:
                animal_list.append(animal + "s")
            else:
                animal_list.append(animal)

        if len(animal_list) == 1:
            animal_str = animal_list[0]
        else:
            animal_str = ", ".join(animal_list[:-1]) + " and " + animal_list[-1]
        return f"{self.name}'s farm has {animal_str}."


macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())
print()
print(macdonald.get_short_info())

print("\n" + "=" * 40 + "\n")

farm2 = Farm("Old MacDonald")
farm2.add_animal(cow=5, sheep=2, goat=12)
print(farm2.get_info())
print()
print(farm2.get_short_info())
