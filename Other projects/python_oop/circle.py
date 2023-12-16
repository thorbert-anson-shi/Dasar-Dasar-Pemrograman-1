from math import pi
class Circle:
    def __init__(self, radius:float = 1) -> None:
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius

    def set_radius(self, radius:int):
        self.radius = radius

    def __str__(self):
        return f"Hello bois"

my_circle = Circle(10)
print(my_circle)
print(my_circle.get_area())
