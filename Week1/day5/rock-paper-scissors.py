from game import Game


def get_user_menu_choice():
    """Affiche le menu et retourne le choix de l'utilisateur ('g' ou 'x')."""
    print("\nMenu :")
    print("(g) Jouer une nouvelle partie")
    print("(x) Afficher les scores et quitter")
    while True:
        choix = input("Votre choix : ").strip().lower()
        if choix in ("g", "x"):
            return choix
        print("Choix invalide. Entrez 'g' ou 'x'.")


def print_results(results):
    """Affiche le résumé des parties jouées."""
    print("\nRésultats des parties :")
    print(f"Vous avez gagné {results['win']} fois")
    print(f"Vous avez perdu {results['loss']} fois")
    print(f"Match nul {results['draw']} fois")
    print("Merci d'avoir joué !")


def main():
    """Fonction principale : boucle du menu, exécution des parties, cumul des scores."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choix = get_user_menu_choice()
        if choix == "g":
            game = Game()
            resultat = game.play()
            results[resultat] += 1
        else:  # choix == 'x'
            print_results(results)
            break


if __name__ == "__main__":
    main()
