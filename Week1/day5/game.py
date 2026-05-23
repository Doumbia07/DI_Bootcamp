import random


class Game:
    def get_user_item(self):
        """Demande à l'utilisateur de choisir pierre, papier ou ciseaux.
        Valide l'entrée et retourne l'item sous forme de chaîne complète.
        """
        choix_valides = {
            "r": "rock",
            "p": "paper",
            "s": "scissors",
            "rock": "rock",
            "paper": "paper",
            "scissors": "scissors",
        }
        while True:
            user_input = (
                input("Choisissez (r)ock, (p)aper, (s)cissors : ").strip().lower()
            )
            if user_input in choix_valides:
                return choix_valides[user_input]
            print("Choix invalide. Veuillez entrer r, p, s, ou le mot complet.")

    def get_computer_item(self):
        """Sélectionne un item aléatoire pour l'ordinateur."""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Détermine le résultat : win, draw ou loss."""
        if user_item == computer_item:
            return "draw"
        # Conditions de victoire
        if (
            (user_item == "rock" and computer_item == "scissors")
            or (user_item == "scissors" and computer_item == "paper")
            or (user_item == "paper" and computer_item == "rock")
        ):
            return "win"
        return "loss"

    def play(self):
        """Exécute une partie complète :
        - choix utilisateur
        - choix ordinateur
        - affichage du résultat
        - retourne win/draw/loss
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        items_fr = {"rock": "pierre", "paper": "papier", "scissors": "ciseaux"}
        user_fr = items_fr[user_item]
        comp_fr = items_fr[computer_item]

        if result == "win":
            print(
                f"Vous avez choisi : {user_fr}. L'ordinateur a choisi : {comp_fr}. Vous gagnez !"
            )
        elif result == "loss":
            print(
                f"Vous avez choisi : {user_fr}. L'ordinateur a choisi : {comp_fr}. Vous perdez."
            )
        else:
            print(
                f"Vous avez choisi : {user_fr}. L'ordinateur a choisi : {comp_fr}. Match nul."
            )

        return result
