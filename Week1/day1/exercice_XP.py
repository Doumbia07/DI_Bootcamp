# EXERCICE 1
print("Hello world\nHello world\nHello world\nHello world")

# EXERCICE 2
result = (99 ** 3) * 8
print(result)

# EXERCICE 3
print(5 < 3)          # False
print(3 == 3)         # True
print(3 == "3")       # False
print("3" > 3)        # TypeError
print("Hello" == "hello")  # False

# EXERCICE 4
computer_brand = "Toshiba"
print("I have a " + computer_brand + " computer.")

# EXERCICE 5
name = "Doumbia"
age = 26
shoe_size = 44
info = f"Je m'appelle {name}, j'ai {age} ans et je chausse du {shoe_size}. J'adore programmer !"
print(info)

# EXERCICE 6
a = 12
b = 8
if a > b:
    print("Hello World")

# EXERCICE 7
nombre = int(input("Donne un nombre entier : "))
if nombre % 2 == 0:
    print("Pair")
else:
    print("Impair")

# EXERCICE 8
mon_nom = "Doumbia"
nom_utilisateur = input("Quel est ton nom ? ")
if mon_nom.lower() == nom_utilisateur.lower():
    print("On a le même nom !")
else:
    print("Salut " + nom_utilisateur + ", moi c'est " + mon_nom + ".")

# EXERCICE 9
taille_cm = int(input("Taille en centimètres : "))
if taille_cm > 145:
    print("Tu es assez grand pour le manège.")
else:
    print("Il faut encore grandir un peu.")