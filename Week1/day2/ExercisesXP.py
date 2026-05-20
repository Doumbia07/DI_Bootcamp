# Exercice 1
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
print(dict(zip(keys, values)))

# Exercice 2
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total = 0
for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(name, ":", price, "$")
    total += price
print("Total cost:", total, "$")

# Bonus Exercice 2 (saisie utilisateur)
family = {}
while True:
    name = input("Enter family member name (or 'quit'): ")
    if name == "quit":
        break
    age = int(input("Enter age: "))
    family[name] = age
total = 0
for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(name, ":", price, "$")
    total += price
print("Total cost:", total, "$")

# Exercice 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": ["blue"], "Spain": ["red"], "US": ["pink", "green"]},
}
brand["number_stores"] = 2
print("Zara sells clothes for", brand["type_of_clothes"])
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(list(brand.keys()))

# Bonus Exercice 3 (fusion)
more_on_zara = {"creation_date": 1975, "number_stores": 7000}
brand.update(more_on_zara)
print(brand)


# Exercice 4
def describe_city(city, country="Unknown"):
    print(city, "is in", country)


describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Tokyo", "Japan")

# Exercice 5
import random


def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success!")
    else:
        print("Fail! Your number:", user_number, "Random number:", random_number)


compare_numbers(50)


# Exercice 6
def make_shirt(size="large", text="I love Python"):
    print("The size of the shirt is", size, "and the text is", text)


make_shirt()
make_shirt("medium")
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")


# Exercice 7
def get_random_temp():
    return random.randint(-10, 40)


def main():
    temp = get_random_temp()
    print("The temperature right now is", temp, "degrees Celsius.")
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp <= 23:
        print("Nice weather.")
    elif temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


main()


# Bonus 4 : température flottante
def get_random_temp_float():
    return round(random.uniform(-10, 40), 1)


temp_float = get_random_temp_float()
print("Float temperature:", temp_float)

# Bonus 5 : saisons
month = int(input("Enter month (1-12): "))
if month in [12, 1, 2]:
    season_temp = random.randint(-10, 10)
elif month in [3, 4, 5]:
    season_temp = random.randint(5, 20)
elif month in [6, 7, 8]:
    season_temp = random.randint(20, 40)
else:
    season_temp = random.randint(5, 20)
print("Season-based temperature:", season_temp)

# Exercice 8
base_price = 10
topping_price = 2.50
toppings = []
while True:
    topping = input("Enter pizza topping (or 'quit'): ")
    if topping == "quit":
        break
    print("Adding", topping, "to your pizza.")
    toppings.append(topping)
print("All toppings:", toppings)
total = base_price + len(toppings) * topping_price
print("Total cost: $", total)
