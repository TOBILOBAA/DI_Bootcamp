import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        """
        Create a circle by giving EITHER radius OR diameter (not both).
        """
        if (radius is None and diameter is None) or (radius is not None and diameter is not None):
            raise ValueError("Provide exactly one of: radius OR diameter")

        # store radius as the single source of truth
        if radius is not None:
            self._radius = float(radius)
        else:
            self._radius = float(diameter) / 2.0

        if self._radius <= 0:
            raise ValueError("Radius must be positive")

    # --- radius / diameter as linked properties ---
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Diameter must be positive")
        self._radius = value / 2.0

    # --- computed attribute ---
    def area(self):
        return math.pi * (self._radius ** 2)

    # --- printing (dunder) ---
    def __str__(self):
        # user-friendly text
        return f"Circle(r={self.radius:.2f}, d={self.diameter:.2f}, area={self.area():.2f})"

    def __repr__(self):
        # debug-friendly text
        return f"Circle(radius={self.radius})"

    # --- arithmetic: add circles -> new circle ---
    def __add__(self, other):
        """
        Circle + Circle -> new Circle with radius = r1 + r2
        Circle + number -> new Circle with radius = r1 + number
        """
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        elif isinstance(other, (int, float)):
            return Circle(radius=self.radius + float(other))
        return NotImplemented

    # support number + Circle
    def __radd__(self, other):
        return self.__add__(other)

    # --- comparisons (so we can check bigger/equal and sort) ---
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return abs(self.radius - other.radius) < 1e-9

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius


# ---------------------------
# Quick demo (you can comment this out in submission)
# ---------------------------
if __name__ == "__main__":
    c1 = Circle(radius=3)
    c2 = Circle(diameter=10)   # radius = 5
    c3 = Circle(radius=4)

    print(c1)                  # prints radius, diameter, area
    print("c1 area:", round(c1.area(), 2))

    c_sum = c1 + c2
    print("c1 + c2 ->", c_sum)

    print("Is c2 bigger than c1?", c2 > c1)   # comparison
    print("Is c1 equal to c3?", c1 == c3)

    circles = [c1, c2, c3, c_sum]
    circles.sort()             # uses __lt__
    print("Sorted by radius:", circles)