from googletrans import Translator  # pyright: ignore[reportMissingImports]

# Liste des mots français
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Création d'un objet traducteur
translator = Translator()

# Dictionnaire pour stocker les résultats
translated_dict = {}

# Traduction de chaque mot français en anglais
for word in french_words:
    translation = translator.translate(word, src="fr", dest="en")
    translated_dict[word] = translation.text

# Affichage du résultat
print(translated_dict)
