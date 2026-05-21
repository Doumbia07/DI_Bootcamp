# CHALLENGE 1 : Dictionnaire d'indices des lettres

mot = input("Entrez un mot : ")

dico = {}

for i, lettre in enumerate(mot):
    if lettre in dico:
        dico[lettre].append(i)
    else:
        dico[lettre] = [i]

print(dico)

# print("\n" + "=" * 50 + "\n")

# CHALLENGE 2 : Articles abordables

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

argent = int(wallet.replace("$", ""))

basket = []

for article, prix_texte in items_purchase.items():
    prix = int(prix_texte.replace("$", "").replace(",", ""))
    if prix <= argent:
        basket.append(article)
        argent = argent - prix

if len(basket) == 0:
    print("Nothing")
else:
    basket_trie = sorted(basket)
    print(basket_trie)
