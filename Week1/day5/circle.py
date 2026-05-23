import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        """
        Crée un cercle soit par le rayon, soit par le diamètre.
        Exemples :
            c = Circle(radius=5)
            c = Circle(diameter=10)
        """
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.diameter = diameter
        else:
            raise ValueError("Vous devez fournir soit 'radius', soit 'diameter'.")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Le rayon doit être positif.")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Le diamètre doit être positif.")
        self._radius = value / 2

    @property
    def area(self):
        """Calcule l'aire du cercle (π × r²)."""
        return math.pi * (self._radius**2)

    def __str__(self):
        """Affichage lisible du cercle."""
        return (
            f"Cercle(rayon={self.radius:.2f}, diamètre={self.diameter:.2f}, "
            f"aire={self.area:.2f})"
        )

    def __repr__(self):
        """Représentation technique pour le débogage."""
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        """Additionne deux cercles (addition des rayons). Retourne un nouveau cercle."""
        if not isinstance(other, Circle):
            raise TypeError("L'addition n'est possible qu'avec un autre Circle.")
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        """Comparateur > (basé sur le rayon)."""
        if not isinstance(other, Circle):
            raise TypeError("Comparaison impossible avec un autre Circle.")
        return self.radius > other.radius

    def __eq__(self, other):
        """Égalité de deux cercles (même rayon)."""
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius

    def __lt__(self, other):
        """Comparateur < (nécessaire pour le tri)."""
        if not isinstance(other, Circle):
            raise TypeError("Comparaison impossible avec un autre Circle.")
        return self.radius < other.radius


if __name__ == "__main__":
    # Création de plusieurs cercles
    c1 = Circle(radius=5)
    c2 = Circle(diameter=8)
    c3 = Circle(radius=7)
    c4 = Circle(diameter=10)

    print("=== Affichage des cercles ===")
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print("\n=== Aire ===")
    print(f"Aire de c1 : {c1.area:.2f}")

    print("\n=== Addition de cercles ===")
    c5 = c1 + c2
    print(f"{c1} + {c2} = {c5}")

    print("\n=== Comparaisons ===")
    print(f"c1 > c2 : {c1 > c2}")  # True
    print(f"c1 < c3 : {c1 < c3}")  # True
    print(f"c1 == c4 : {c1 == c4}")  # True (même rayon 5)
    print(f"c1 == c2 : {c1 == c2}")  # False

    print("\n=== Tri d'une liste de cercles ===")
    cercles = [c3, c1, c2, c5]  # rayons : 7, 5, 4, 9
    cercles_tries = sorted(cercles)
    print("Avant tri :", [c.radius for c in cercles])
    print("Après tri :", [c.radius for c in cercles_tries])
    print("Détail des cercles triés :")
    for c in cercles_tries:
        print(f"  {c}")
