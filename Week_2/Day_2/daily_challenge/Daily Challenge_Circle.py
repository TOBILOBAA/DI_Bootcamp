import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        """Initialize circle with either radius or diameter."""
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = 1  # default

    @property
    def diameter(self):
        """Return diameter (always 2*radius)."""
        return self.radius * 2

    @property
    def area(self):
        """Return circle area."""
        return math.pi * (self.radius ** 2)

    # -------------------------------
    # Dunder methods
    # -------------------------------
    def __str__(self):
        """Readable string (when using print)."""
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __add__(self, other):
        """Add two circles → new circle with summed radii."""
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        """Equality: True if radii are equal."""
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        """Less-than: compare radii (so we can sort)."""
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented
    

if __name__ == "__main__":
    c1 = Circle(radius=5)
    c2 = Circle(diameter=10)
    c3 = Circle(radius=7)

    # Print circles
    print(c1)  # Circle(radius=5.00, diameter=10.00, area=78.54)
    print(c2)  # Circle(radius=5.00, diameter=10.00, area=78.54)
    print(c3)  # Circle(radius=7.00, diameter=14.00, area=153.94)

    # Add circles
    c4 = c1 + c3
    print("c1 + c3 =", c4)

    # Compare
    print("c1 == c2:", c1 == c2)   # True
    print("c1 < c3:", c1 < c3)     # True
    print("c3 > c2:", c3 > c2)     # True (because of __lt__)

    # Sorting
    circles = [c3, c1, c2, c4]
    circles.sort()
    print("\nSorted circles (by radius):")
    for c in circles:
        print(c)



import turtle

def draw_circles(circles):
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(0)

    y_offset = 0
    for circle in circles:
        pen.penup()
        pen.goto(0, -circle.radius - y_offset)
        pen.pendown()
        pen.circle(circle.radius)
        y_offset += 20  # small spacing between circles

    screen.mainloop()

if __name__ == "__main__":
    # After creating circles
    draw_circles(circles)  # will open Turtle window