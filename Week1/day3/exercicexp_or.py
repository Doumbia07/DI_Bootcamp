import random


# Exercise 1: Circle
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.1416 * self.radius

    def area(self):
        return 3.1416 * self.radius**2

    def definition(self):
        print(
            "A circle is a round plane figure whose boundary (the circumference) consists of points equidistant from a fixed point (the center)."
        )


# Exercise 2: MyList
class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reversed_list(self):
        return self.letters[::-1]

    def sorted_list(self):
        return sorted(self.letters)

    def random_numbers_list(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]


# Exercise 3: MenuManager
class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
        ]

    def add_item(self, name, price, spice, gluten):
        new_item = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_item)
        print(f"{name} has been added to the menu.")

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                print(f"{name} has been updated.")
                return
        print(f"{name} is not on the menu.")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                print(f"{name} has been removed. Updated menu:")
                for dish in self.menu:
                    print(dish)
                return
        print(f"{name} is not on the menu.")
