# Importation du module datetime pour manipuler les dates
import datetime

# ---------- 1. Demander la date de naissance ----------
print("Entrez votre date de naissance au format JJ/MM/AAAA (exemple : 15/03/1990)")
date_str = input("> ")

# Découper la chaîne en jour, mois, année
jour, mois, annee = date_str.split('/')
jour = int(jour)
mois = int(mois)
annee = int(annee)

# ---------- 2. Calculer l'âge ----------
# Date d'aujourd'hui
aujourdhui = datetime.date.today()

# Construire la date de naissance de cette année (pour comparer mois/jour)
naissance_cette_annee = datetime.date(aujourdhui.year, mois, jour)

# Si la date d'anniversaire de cette année est après aujourd'hui, l'anniversaire n'est pas encore passé
if naissance_cette_annee > aujourdhui:
    age = aujourdhui.year - annee - 1
else:
    age = aujourdhui.year - annee

# ---------- 3. Dernier chiffre de l'âge ----------
dernier_chiffre = age % 10

# ---------- 4. Construire la ligne des bougies ----------
# La ligne de base dans le dessin : "       ___iiiii___"
# On va remplacer "iiiii" par 'i' répété `dernier_chiffre` fois
bougies = 'i' * dernier_chiffre
# On garde les 3 underscores avant et après
ligne_bougies = f"       ___{bougies}___"

# Mais attention : dans le dessin original, il y a 7 espaces avant "___iiiii___" ?
# Regardons le dessin :
"""
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
# La première ligne a 7 espaces puis "___iiiii___". Donc on garde 7 espaces + le reste.

# ---------- 5. Afficher le gâteau ----------
# On imprime chaque ligne exactement comme dans l'énoncé, sauf la première qui change.
print(f"      ___{bougies}___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")

# ---------- 6. Bonus : année bissextile ----------
# Une année est bissextile si divisible par 4, pas par 100, sauf si divisible par 400.
bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

if bissextile:
    print("\n" + "=" * 30)  # séparation entre les deux gâteaux
    print("🎂 Année bissextile ! Deuxième gâteau : 🎂\n")
    # On réaffiche le même gâteau (mêmes bougies)
    print(f"    ___{bougies}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

# ---------- Affichage supplémentaire : l'âge ----------
print(f"\nTu as {age} ans, donc {dernier_chiffre} bougie(s) sur le gâteau.")
if bissextile:
    print("(Bonus : tu es né(e) une année bissextile, donc deux gâteaux !)")