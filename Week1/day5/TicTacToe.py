# TicTacToe


def display_board(board):
    """Affiche le plateau de jeu."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def player_input(board, player):
    """
    Demande au joueur (X ou O) de choisir une case (1-9).
    Vérifie que la case est libre et valide.
    Retourne l'indice (0-8) de la case choisie.
    """
    while True:
        try:
            choice = int(input(f"Joueur {player}, choisissez une case (1-9) : "))
            if choice < 1 or choice > 9:
                print("Veuillez entrer un nombre entre 1 et 9.")
                continue
            index = choice - 1
            if board[index] != " ":
                print("Cette case est déjà occupée. Choisissez-en une autre.")
                continue
            return index
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")


def check_win(board, player):
    """
    Vérifie si le joueur donné a gagné.
    Retourne True si trois symboles alignés, sinon False.
    """
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # lignes
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # colonnes
        [0, 4, 8],
        [2, 4, 6],  # diagonales
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_board_full(board):
    """Retourne True si toutes les cases sont occupées."""
    return all(cell != " " for cell in board)


def play():
    """Fonction principale qui gère une partie de Morpion."""
    board = [" "] * 9
    current_player = "X"
    game_over = False

    print("Bienvenue dans le jeu du Morpion !")
    display_board(board)

    while not game_over:
        index = player_input(board, current_player)
        board[index] = current_player
        display_board(board)

        if check_win(board, current_player):
            print(f"Félicitations ! Le joueur {current_player} a gagné !")
            game_over = True
        elif is_board_full(board):
            print("Match nul ! Le plateau est plein.")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

    print("Partie terminée. Merci d'avoir joué !")


if __name__ == "__main__":
    play()
