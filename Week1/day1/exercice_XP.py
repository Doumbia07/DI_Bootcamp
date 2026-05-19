# Exercice 1 : Hello World
print("Hello world\n" * 4)
# Exercice 2 : Some Math
result = (99 ** 3) * 8
print(result)

# Exercice 3 : What is the output ?

print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
print("3" > 3)   #TypeError
print("Hello" == "hello") #False

# Exercice 4 : Your computer brand
computer_brand = "Toshiba"   
print("I have a " + computer_brand + " computer.")

# Exercice 5 : Your information
name = "Doumbia"
age = 26
shoe_size = 44
info = f"Je m'appelle {name}, j'ai {age} ans et je chausse du {shoe_size}. J'adore programmer !"
print(info)

# Exercice 6 : A & B
a = 12
b = 8
if a > b:
    print("Hello World")

# Exercice 7 : Odd or Even
nombre = int(input("Donne un nombre entier : "))
if nombre % 2 == 0:
    print("Pair")
else:
    print("Impair")

# Exercice 8 : What’s your name ?
mon_nom = "Doumbia"
nom_utilisateur = input("Quel est ton nom ? ")
if mon_nom.lower() == nom_utilisateur.lower():
    print("On a le même nom")
else:
    print("Salut " + nom_utilisateur + ", moi c'est " + mon_nom + ".")

# Exercice 9 : Tall enough to ride a roller coaster
taille_cm = int(input("Taille en centimètres : "))
if taille_cm > 145:
    print("Tu es assez grand pour le manège.")
else:
    print("Il faut encore grandir un peu.")