# Challenge 1 :
entree = input("Entrez des mots séparés par des virgules : ")
mots = [mot.strip() for mot in entree.split(",")]  # liste en compréhension
mots_tries = sorted(mots)
print(",".join(mots_tries))


# Challenge 2 : Trouver le mot le plus long
def longest_word(sentence):
    mots = sentence.split()
    return max(mots, key=len)


print("=== Challenge 2 : Trouver le mot le plus long ===")

# Exemples de test
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
