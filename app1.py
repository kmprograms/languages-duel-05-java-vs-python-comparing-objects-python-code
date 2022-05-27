import math
from dataclasses import dataclass

"""
    Przygotuj strukturę danych, która przechowuje współrzędne punktu 
    w układzie współrzędnych. Aplikacja umożliwia porównywanie obiektów 
    tej struktury danych. Kryterium porównywania jest odległość punktu
    od początku układu współrzędnych.
"""


@dataclass
class Point:
    x: float
    y: float

    def get_zero_distance(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return isinstance(other, Point) and \
               self.get_zero_distance() < other.get_zero_distance()

    def __le__(self, other):
        return isinstance(other, Point) and \
               self.get_zero_distance() <= other.get_zero_distance()

    def __eq__(self, other):
        return isinstance(other, Point) and \
               self.get_zero_distance() == other.get_zero_distance()

    def __hash__(self):
        return hash((self.get_zero_distance(), ))

def main() -> None:
    p1 = Point(x=1, y=1)
    p2 = Point(x=1, y=1)
    p3 = Point(x=2, y=2)
    p4 = Point(x=1, y=2)
    p5 = Point(x=2, y=1)

    print(p1 == p2)
    print(p4 == p5)
    print(p1 != p3)
    print(p1 < p3)
    print(p1 <= p2)
    print(p3 > p1)
    print(p2 >= p1)


if __name__ == '__main__':
    main()
