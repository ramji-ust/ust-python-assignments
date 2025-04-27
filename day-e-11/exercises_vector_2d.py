class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __str__(self):
        return f"({self.x}, {self.y})"

# Testing the class
if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    v3 = v1 + v2   # Should be (4, 6)
    v4 = v1 - v2   # Should be (2, 2)

    print("v3:", v3)  # (4, 6)
    print("v4:", v4)  # (2, 2)
    print(v3 == Vector2D(4, 6))  # True
    print(v4 == Vector2D(2, 2))  # True
    print(v3 == v4)  # False
