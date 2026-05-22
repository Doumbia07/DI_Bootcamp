import copy
import random
import time
import os


class GameOfLife:
    def __init__(self, width, height, fixed_borders=True, max_size=10000):
        self.width = width
        self.height = height
        self.fixed_borders = fixed_borders
        self.max_size = max_size
        self.grid = [[False for _ in range(width)] for _ in range(height)]

    def set_cell(self, x, y, alive):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = alive

    def random_fill(self, density=0.2):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = random.random() < density

    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = False

    def count_neighbors(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if self.fixed_borders:
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if self.grid[ny][nx]:
                            count += 1
                else:
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if self.grid[ny][nx]:
                            count += 1
        return count

    def _expand_if_needed(self):
        # Vérifie si des cellules vivantes sont sur les bords
        expand_top = (
            any(self.grid[0][x] for x in range(self.width))
            if self.height > 0
            else False
        )
        expand_bottom = (
            any(self.grid[self.height - 1][x] for x in range(self.width))
            if self.height > 0
            else False
        )
        expand_left = (
            any(self.grid[y][0] for y in range(self.height))
            if self.width > 0
            else False
        )
        expand_right = (
            any(self.grid[y][self.width - 1] for y in range(self.height))
            if self.width > 0
            else False
        )

        new_h = self.height
        new_w = self.width
        if expand_top and self.height + 1 <= self.max_size:
            new_h += 1
        if expand_bottom and self.height + 1 <= self.max_size:
            new_h += 1
        if expand_left and self.width + 1 <= self.max_size:
            new_w += 1
        if expand_right and self.width + 1 <= self.max_size:
            new_w += 1

        if new_h != self.height or new_w != self.width:
            # Création de la nouvelle grille
            new_grid = [[False for _ in range(new_w)] for _ in range(new_h)]
            y_offset = 1 if expand_top else 0
            x_offset = 1 if expand_left else 0
            for y in range(self.height):
                for x in range(self.width):
                    new_grid[y + y_offset][x + x_offset] = self.grid[y][x]
            self.grid = new_grid
            self.height = new_h
            self.width = new_w

    def next_generation(self):
        if not self.fixed_borders:
            self._expand_if_needed()
        # Dimensions actuelles après expansion possible
        rows, cols = self.height, self.width
        new_grid = [[False for _ in range(cols)] for _ in range(rows)]
        for y in range(rows):
            for x in range(cols):
                neighbors = self.count_neighbors(x, y)
                alive = self.grid[y][x]
                if alive:
                    new_grid[y][x] = neighbors == 2 or neighbors == 3
                else:
                    new_grid[y][x] = neighbors == 3
        self.grid = new_grid

    def display(self, clear_screen=True):
        if clear_screen:
            os.system("cls" if os.name == "nt" else "clear")
        print("+" + "-" * self.width + "+")
        for row in self.grid:
            print("|" + "".join("█" if cell else " " for cell in row) + "|")
        print("+" + "-" * self.width + "+")

    def run(self, generations=100, delay=0.2):
        for gen in range(generations):
            self.display()
            print(f"Generation: {gen} | Size: {self.width}x{self.height}")
            time.sleep(delay)
            self.next_generation()
            if not any(any(row) for row in self.grid):
                print("All cells are dead. Game over.")
                break


if __name__ == "__main__":
    # Exemple 1 : Blinker (oscillateur) bords fixes
    print("=== Blinker (fixed borders) ===")
    game1 = GameOfLife(5, 5, fixed_borders=True)
    game1.set_cell(1, 2, True)
    game1.set_cell(2, 2, True)
    game1.set_cell(3, 2, True)
    game1.run(generations=4, delay=0.5)

    # Exemple 2 : Planeur (glider) bords extensibles
    print("\n=== Glider (expandable borders) ===")
    game2 = GameOfLife(5, 5, fixed_borders=False, max_size=20)
    # Motif planeur
    game2.set_cell(1, 0, True)
    game2.set_cell(2, 1, True)
    game2.set_cell(0, 2, True)
    game2.set_cell(1, 2, True)
    game2.set_cell(2, 2, True)
    game2.run(generations=30, delay=0.2)
